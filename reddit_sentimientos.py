import praw
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

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
query = "Uribismo = Petrismo"
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
df.to_csv("reddit_sentimientos.csv", index=False, encoding="utf-8")

# Mostrar un resumen de los resultados
print(df["Sentimiento"].value_counts())
print("Análisis de sentimientos completado. Resultados guardados en 'reddit_sentimientos.csv'.")