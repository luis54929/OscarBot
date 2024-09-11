import pandas as pd
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import sqlite3
import pickle
import os

from utils import preprocess_text, ContextManager, save_trained_model, load_trained_model, create_chatbot

def main():
    # Cargar o crear OscarBot
    oscarbot = load_trained_model()

    # Cargar datos si es necesario
    if not os.path.exists('trained_model.pkl'):
        print("Cargando y procesando datos...")
        df1 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_196.csv')
        df2 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_301.csv')
        df = pd.concat([df1, df2])
        df['text'] = df['text'].astype(str)
        train_chatbot(oscarbot, df['text'])

    context_manager = ContextManager()
    
    print("OscarBot: Hola! ¿Cómo puedo ayudarte hoy?")
    
    while True:
        try:
            user_input = input("Tú: ")
            processed_input = preprocess_text(user_input)
            response = oscarbot.get_response(processed_input)
            context_manager.update_context(user_input, str(response))
            print(f"OscarBot: {response}")
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            save_trained_model(oscarbot)
            break

if __name__ == "__main__":
    main()
