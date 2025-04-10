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
""" 
praw-Biblioteca Python que permite interactuar con la
    API de Reddit de manera sencilla. 
    Es como un puente entre tu programa y Reddit, 
    lo que te permite automatizar tareas o extraer datos de esta plataforma.

matplotlib.pyplot usado para montar informe de barras
    """

#Este es el analizador de sentimientos de VADER 
# (Valence Aware Dictionary and sEntiment Reasoner), 
# que se utiliza para calcular el sentimiento de un texto.

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import praw
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os
import textwrap
#textwrap para manipulación de textos

# Descargar los datos necesarios para VADER
nltk.download('vader_lexicon')

# Configurar la conexión con Reddit
reddit = praw.Reddit(
    client_id="4gitJskjt121GuCBhB2_7g",       # Reemplaza con tu Client ID
    client_secret="zyL2beX4J2-14O79HG_Re_IZZSAz_g",  # Reemplaza con tu Client Secret
    user_agent="AnalisisSentimientoParaClase"  # Nombre de tu aplicación
)

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "¡Hola! Soy tu bot de análisis de sentimientos en Reddit.\n"
        "Usa el comando /buscar seguido del enunciado que deseas analizar.\n\n"
        "Por ejemplo:\n"
        "/buscar Uribismo = Petrismo\n\n"
        "¡Estoy listo para ayudarte!"
    )

# Función para el comando /buscar
async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if not context.args:
            await update.message.reply_text(
                "Por favor, proporciona un enunciado para buscar. Ejemplo:\n"
                "/buscar Uribismo = Petrismo"
            )
            return

        query = " ".join(context.args)  # Combina los argumentos en un solo texto
        await update.message.reply_text(f"Buscando publicaciones relacionadas con: {query}...")

        # Buscar publicaciones en Reddit
        subreddit = reddit.subreddit("all")
        posts = subreddit.search(query, limit=100)

        # Buscar el post que coincida exactamente con el enunciado
        post_encontrado = None
        for post in posts:
            if post.title.strip().lower() == query.strip().lower():
                post_encontrado = post
                break

        if post_encontrado:
            # Analizar el sentimiento del post
            sentimiento_post = sia.polarity_scores(post_encontrado.title + " " + post_encontrado.selftext)
            resumen_post = (
                f"Post encontrado:\n"
                f"Título: {post_encontrado.title}\n"
                f"Texto: {post_encontrado.selftext}\n"
                f"Upvotes: {post_encontrado.score}\n"
                f"Número de comentarios: {post_encontrado.num_comments}\n\n"
                f"Sentimiento del post:\n"
                f"Positivo: {sentimiento_post['pos']}\n"
                f"Neutral: {sentimiento_post['neu']}\n"
                f"Negativo: {sentimiento_post['neg']}\n"
                f"Compound: {sentimiento_post['compound']}\n"
            )
            await update.message.reply_text(resumen_post)

            # Analizar los comentarios
            comentarios_data = []
            post_encontrado.comments.replace_more(limit=0)
            comentarios = post_encontrado.comments.list()[:50]  # Analizar solo los primeros 50 comentarios
            for comentario in comentarios:
                sentimiento_comentario = sia.polarity_scores(comentario.body)
                comentarios_data.append({
                    "Comentario": comentario.body,
                    "Upvotes": comentario.score,
                    "Sentimiento": "Positivo" if sentimiento_comentario["compound"] > 0 else "Negativo" if sentimiento_comentario["compound"] < 0 else "Neutral",
                    "Puntaje Sentimiento": sentimiento_comentario["compound"]
                })

            # Convertir los datos de los comentarios en un DataFrame
            df_comentarios = pd.DataFrame(comentarios_data)

            # Resumen de sentimientos
            conteo_sentimientos = df_comentarios["Sentimiento"].value_counts()
            resumen_comentarios = (
                f"\nResumen de sentimientos en los comentarios:\n"
                f"{conteo_sentimientos.to_string()}\n"
            )
            await update.message.reply_text(resumen_comentarios)

            # Comentarios más positivos y negativos
            comentario_positivo = df_comentarios.loc[df_comentarios["Puntaje Sentimiento"].idxmax()]
            comentario_negativo = df_comentarios.loc[df_comentarios["Puntaje Sentimiento"].idxmin()]
            await update.message.reply_text(
                f"Comentario más positivo:\n{comentario_positivo['Comentario']}\n"
                f"Puntaje: {comentario_positivo['Puntaje Sentimiento']}\n\n"
                f"Comentario más negativo:\n{comentario_negativo['Comentario']}\n"
                f"Puntaje: {comentario_negativo['Puntaje Sentimiento']}"
            )
        else:
            await update.message.reply_text("No se encontró ningún post que coincida exactamente con el enunciado proporcionado.")
    except Exception as e:
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud. Por favor, intenta nuevamente.")

# Configurar el bot de Telegram
TOKEN = "7598902574:AAESB4iNYDnrqPvjsywQe4nL8s00hnLRCAk"
app = Application.builder().token(TOKEN).build()

# Agregar manejadores de comandos
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buscar", buscar))

# Iniciar el bot
print("Bot iniciado...")
app.run_polling()
# 