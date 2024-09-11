import pandas as pd
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sqlite3
import pickle
import os

# Cargar spaCy
nlp = spacy.load("en_core_web_sm")

# Función para preprocesar texto
def preprocess_text(text, index=0, total=1):
    doc = nlp(text)
    if index % 1000000 == 0:
        print(f"Procesando texto {index + 1} de {total}")
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

# Clase para manejar el contexto
class ContextManager:
    def __init__(self):
        self.context = []

    def update_context(self, user_input, bot_response):
        self.context.append({"user": user_input, "bot": bot_response})
        if len(self.context) > 10:
            self.context.pop(0)

    def get_context(self):
        return self.context

# Función para guardar el modelo entrenado
def save_trained_model(chatbot, filename='trained_model.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(chatbot, f)
    print(f"Modelo guardado como {filename}")

# Función para cargar el modelo entrenado
def load_trained_model(filename='trained_model.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        print(f"No se encontró el archivo {filename}. Creando un nuevo chatbot.")
        return create_chatbot()

# Función para crear un nuevo chatbot
def create_chatbot():
    return ChatBot(
        'OscarBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'
        ],
        database_uri='sqlite:///database.sqlite3'
    )

# Función para entrenar el chatbot
def train_chatbot(chatbot, data):
    trainer = ListTrainer(chatbot)
    for text in data:
        trainer.train([preprocess_text(text)])
    save_trained_model(chatbot)

# Función principal
def main():
    # Cargar o crear el chatbot
    chatbot = load_trained_model()

    # Cargar datos si es necesario
    if not os.path.exists('trained_model.pkl'):
        print("Cargando y procesando datos...")
        df1 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_196.csv')
        df2 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_301.csv')
        df = pd.concat([df1, df2])
        df['text'] = df['text'].astype(str)
        train_chatbot(chatbot, df['text'])

    context_manager = ContextManager()
    
    print("OscarBot: Hola! ¿Cómo puedo ayudarte hoy?")
    
    while True:
        try:
            user_input = input("Tú: ")
            processed_input = preprocess_text(user_input)
            response = chatbot.get_response(processed_input)
            context_manager.update_context(user_input, str(response))
            print(f"OscarBot: {response}")
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            save_trained_model(chatbot)
            break

if __name__ == "__main__":
    main()