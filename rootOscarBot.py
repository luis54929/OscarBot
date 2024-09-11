import pandas as pd
import spacy

# Cargar el modelo de spaCy
print("Cargando el modelo de spaCy...")
nlp = spacy.load("en_core_web_sm")
print("Modelo cargado.")

# Cargar los datasets
print("Cargando los datasets...")
df1 = pd.read_csv('C:\\OscarBot\\archive\\Ubuntu-dialogue-corpus\\dialogueText_196.csv')
df2 = pd.read_csv('C:\\OscarBot\\archive\\Ubuntu-dialogue-corpus\\dialogueText_301.csv')
print("Datasets cargados.")

# Combinar los datasets
print("Combinando los datasets...")
df = pd.concat([df1, df2])
print("Datasets combinados. Número de filas:", df.shape[0])

# Asegurarse de que todos los valores en la columna 'text' sean cadenas de texto
print("Convirtiendo la columna 'text' a cadenas de texto...")
df['text'] = df['text'].astype(str)
print("Conversión completada.")

print(df.head())

# Preprocesar el texto con progreso
def preprocess_text(text, index, total):
    doc = nlp(text)
    if index % 100 == 0:  # Imprimir cada 100 textos procesados
        print(f"Procesando texto {index + 1} de {total}")
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

print("Preprocesando el texto...")
total_texts = len(df)
df['processed_text'] = [preprocess_text(text, i, total_texts) for i, text in enumerate(df['text'])]
print("Texto preprocesado.")

# Mostrar las primeras filas del dataset procesado
print("Primeras filas del dataset procesado:")
print(df.head())
