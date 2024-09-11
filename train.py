import pandas as pd
from chatterbot.trainers import ListTrainer
from utils import preprocess_text, load_trained_model, save_trained_model

def train_chatbot(chatbot, data):
    trainer = ListTrainer(chatbot)
    for text in data:
        trainer.train([preprocess_text(text)])
    save_trained_model(chatbot)

def main():
    print("Iniciando el entrenamiento de OscarBot...")
    
    # Cargar OscarBot
    oscarbot = load_trained_model()
    
    # Cargar datos de entrenamiento
    print("Cargando datos de entrenamiento...")
    df1 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_196.csv')
    df2 = pd.read_csv('archive/Ubuntu-dialogue-corpus/dialogueText_301.csv')
    df = pd.concat([df1, df2])
    df['text'] = df['text'].astype(str)
    
    # Entrenar OscarBot
    print("Entrenando OscarBot...")
    train_chatbot(oscarbot, df['text'])
    
    print("Entrenamiento completado. OscarBot está listo para usar.")

if __name__ == "__main__":
    main()
