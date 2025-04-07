# Codigo para presentación de tema Técnicas de Machine Learning y Cuándo Usarlas
#  Análisis de sentimientos en redes sociales. SALA 5 
# Autorres : Grupo 12  Escrito WE-FERIA

import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Descargar los datos necesarios para VADER
nltk.download('vader_lexicon')

# Cargar el archivo CSV
df = pd.read_csv("tweets_alvaro_uribe.csv")

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Analizar el sentimiento de cada tweet
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