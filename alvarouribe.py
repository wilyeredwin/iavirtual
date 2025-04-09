# Codigo para presentación de tema Técnicas de Machine Learning y Cuándo Usarlas
#  Análisis de sentimientos en redes sociales. SALA 5 
# Autorres : Grupo 12  Escrito WE-FERIA

import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
""" Natural Language Toolkit -nltk 
    biblioteca de Python diseñada para trabajar 
    con procesamiento de lenguaje natural (NLP).
    Es una herramienta poderosa que permite analizar, 
    procesar y comprender texto en lenguaje humano.
"""
# Descargar los datos necesarios para VADER(veider)
nltk.download('vader_lexicon')
"""VADER (Valence Aware Dictionary and sEntiment Reasoner)
    para determinar si un texto es positivo, negativo o neutral."""
# Cargar el archivo CSV
df = pd.read_csv("tweets_alvaro_uribe.csv")

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Analizar el sentimiento de cada tweet  -compound (compáund)
"""
El compound es un puntaje calculado por el analizador de sentimientos VADER
es un valor numérico que combina los puntajes de sentimiento positivo,
negativo y neutral en un solo número, se mueve entre -1 y 1. 
-1: Sentimiento extremadamente negativo.
 0: Sentimiento neutral.
 1: Sentimiento extremadamente positivo.
 -------------------------------------
compound > 0: El texto tiene un sentimiento positivo.
compound < 0: El texto tiene un sentimiento negativo.
compound == 0: El texto tiene un sentimiento neutral.
Ejemplo: 

Texto: "Me encanta este producto, es increíble!!!"

Palabras analizadas:
"Me encanta" → +1.5
"increíble" → +2.0
"!!!" → Intensifica el sentimiento.
Suma de puntajes:

Total: +1.5 + 2.0 = +3.5.
Normalización: compound = 3.5 / sqrt(3.5^2 + 15)
               compound = 3.5 / sqrt(12.25 + 15)
               compound = 3.5 / sqrt(27.25)
               compound = 3.5 / 5.22
               compound ≈ 0.67
               VADER ajusta el puntaje para reflejar intensidad del "!!!",
               Tambien usa contextos,Peso de las palabras...
               lo que resulta en un valor más alto (0.7783). 

compound = +0.7783 (positivo).
"""

def analizar_sentimiento(texto):
    puntajes = sia.polarity_scores(texto)
    if puntajes['compound'] > 0:
        return "Positivo"
    elif puntajes['compound'] < 0:
        return "Negativo"
    else:
        return "Neutral"

# Aplicar el análisis de sentimientos a la columna "Contenido"
df["Sentimiento"] = df["Contenido"].apply(analizar_sentimiento)

# Guardar los resultados en un nuevo archivo CSV
df.to_csv("tweets_analizados.csv", index=False, encoding="utf-8")

# Mostrar un resumen de los resultados
print(df["Sentimiento"].value_counts())
print("Análisis de sentimientos completado. Resultados guardados en 'tweets_analizados.csv'.")