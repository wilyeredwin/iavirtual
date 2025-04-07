
"""
Que hacer antes...
Ve a Reddit Apps. https://www.reddit.com/prefs/apps
Haz clic en "Create App" o "Create Another App".
Completa los campos:
Name: Un nombre para tu aplicación (por ejemplo, "Análisis de Sentimientos").
App type: Selecciona script.
Redirect URI: Usa http://localhost (o cualquier URL válida).
Description: Opcional.
Guarda la aplicación y copia:
Client ID: Es el código que aparece debajo del nombre de tu aplicación.
Client Secret: Es el código secreto que aparece al lado de tu aplicación.
"""
import praw
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

# Descargar los datos necesarios para VADER
nltk.download('vader_lexicon')

# Configurar la conexión con Reddit
reddit = praw.Reddit(
    client_id="4gitJskjt121GuCBhB2_7g",       # Reemplaza con tu Client ID
    client_secret="zyL2beX4J2-14O79HG_Re_IZZSAz_g",  # Reemplaza con tu Client Secret
    user_agent="AnalisisSentimientoParaClase"  # Nombre de tu aplicación
)


# Buscar publicaciones relacionadas con el tema
subreddit = reddit.subreddit("all")  # Puedes especificar un subreddit, como "Colombia"
query = input("Digite un tema que buscar en la red social REDDIT")
posts = subreddit.search(query, limit=100)


# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Analizar el sentimiento de cada publicación
data = []
for post in posts:
    sentimiento = sia.polarity_scores(post.title + " " + post.selftext)
    data.append({
        "Título": post.title,
        "Texto": post.selftext,
        "Upvotes": post.score,
        "Comentarios": post.num_comments,
        "Sentimiento": "Positivo" if sentimiento["compound"] > 0 else "Negativo" if sentimiento["compound"] < 0 else "Neutral",
        "Puntaje Sentimiento": sentimiento["compound"]
    })

# Convertir los datos en un DataFrame
df = pd.DataFrame(data)

# Guardar los resultados en un archivo CSV
Archivo =input("Digite el nombre del archivo donde guardar los resultados")
df.to_csv(f"{Archivo}.csv", index=False, encoding="utf-8")

# Mostrar un resumen de los resultados
print(df["Sentimiento"].value_counts())
print(f"Análisis de sentimientos completado. Resultados guardados en '{Archivo}.csv'.")


