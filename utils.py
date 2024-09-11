import spacy
import pickle
import os
from chatterbot import ChatBot

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text, index=0, total=1):
    doc = nlp(text)
    if index % 1000000 == 0:
        print(f"Procesando texto {index + 1} de {total}")
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

class ContextManager:
    def __init__(self):
        self.context = []

    def update_context(self, user_input, bot_response):
        self.context.append({"user": user_input, "bot": bot_response})
        if len(self.context) > 10:
            self.context.pop(0)

    def get_context(self):
        return self.context

def save_trained_model(chatbot, filename='trained_model.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(chatbot, f)
    print(f"Modelo guardado como {filename}")

def load_trained_model(filename='trained_model.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        print(f"No se encontró el archivo {filename}. Creando un nuevo OscarBot.")
        return create_chatbot()

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
