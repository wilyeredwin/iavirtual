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

import praw
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os
import matplotlib.pyplot as plt
import textwrap

# Descargar los datos necesarios para VADER
nltk.download('vader_lexicon')

# Configurar la conexión con Reddit
reddit = praw.Reddit(
    client_id="4gitJskjt121GuCBhB2_7g",       # Reemplaza con tu Client ID
    client_secret="zyL2beX4J2-14O79HG_Re_IZZSAz_g",  # Reemplaza con tu Client Secret
    user_agent="AnalisisSentimientoParaClase"  # Nombre de tu aplicación
)

# Solicitar el enunciado exacto al usuario
query = input("Digite el enunciado exacto que desea buscar en Reddit: ")

# Buscar publicaciones relacionadas con el enunciado exacto
subreddit = reddit.subreddit("all")  # Puedes especificar un subreddit, como "Colombia"
posts = subreddit.search(query, limit=100)

# Inicializar el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Buscar el post que coincida exactamente con el enunciado
post_encontrado = None
for post in posts:
    if post.title.strip().lower() == query.strip().lower():
        post_encontrado = post
        break

if post_encontrado:
    print(f"\nPost encontrado: {post_encontrado.title}")
    print(f"Texto: {post_encontrado.selftext}")
    print(f"Upvotes: {post_encontrado.score}")
    print(f"Número de comentarios: {post_encontrado.num_comments}")

    # Analizar el sentimiento del post
    sentimiento_post = sia.polarity_scores(post_encontrado.title + " " + post_encontrado.selftext)
    print("\nSentimiento del post:")
    print(f"Positivo: {sentimiento_post['pos']}")
    print(f"Neutral: {sentimiento_post['neu']}")
    print(f"Negativo: {sentimiento_post['neg']}")
    print(f"Compound: {sentimiento_post['compound']}")

    # Analizar los comentarios del post
    print("\nAnalizando comentarios...")
    comentarios_data = []
    post_encontrado.comments.replace_more(limit=None)  # Cargar todos los comentarios
    for comentario in post_encontrado.comments.list():
        sentimiento_comentario = sia.polarity_scores(comentario.body)
        comentarios_data.append({
            "Comentario": comentario.body,
            "Upvotes": comentario.score,
            "Sentimiento": "Positivo" if sentimiento_comentario["compound"] > 0 else "Negativo" if sentimiento_comentario["compound"] < 0 else "Neutral",
            "Puntaje Sentimiento": sentimiento_comentario["compound"]
        })

    # Convertir los datos de los comentarios en un DataFrame
    df_comentarios = pd.DataFrame(comentarios_data)

    # Guardar los resultados en un archivo CSV
    archivo_comentarios = "comentarios_analizados.csv"
    df_comentarios.to_csv(archivo_comentarios, index=False, encoding="utf-8")

    # Mostrar un resumen de los resultados
    print("\nResumen de sentimientos de los comentarios:")
    print(df_comentarios["Sentimiento"].value_counts())
    print(f"Análisis de comentarios completado. Resultados guardados en '{archivo_comentarios}'.")

   
    # -------------------------------------------------------
    # Montaje de informe sobre información
    df = pd.read_csv(archivo_comentarios, encoding="utf-8")

    # Verificar las primeras filas del archivo
    print("Primeras filas del archivo:")
    print(df.head())

    # Resumen de sentimientos
    print("\nResumen de sentimientos:")
    conteo_sentimientos = df["Sentimiento"].value_counts()
    print(conteo_sentimientos)

    # Estadísticas descriptivas de los puntajes de sentimiento
    print("\nEstadísticas descriptivas de los puntajes de sentimiento:")
    print(df["Puntaje Sentimiento"].describe())

    # Gráfico de barras para la distribución de sentimientos
    plt.figure(figsize=(8, 6))
    # Se crea el grafico con la serie conteo_sentimientos
    conteo_sentimientos.plot(kind="bar", color=["green", "red", "blue"])
    titulo = "Distribución de Sentimientos en los Comentarios ("+post_encontrado.title+")"
    titulo_envuelto = "\n".join(textwrap.wrap(titulo, width=60))  # Ajusta el ancho con `width`
    plt.title(titulo_envuelto, loc="center")
    plt.xlabel("Sentimiento")
    plt.ylabel("Cantidad de Comentarios")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("grafico_sentimientos.png")  # Guardar el gráfico como imagen
    plt.show()

    # Comentarios más positivos y más negativos
    comentario_positivo = df.loc[df["Puntaje Sentimiento"].idxmax()]
    comentario_negativo = df.loc[df["Puntaje Sentimiento"].idxmin()]

    print("\nComentario más positivo:")
    print(f"Comentario: {comentario_positivo['Comentario']}")
    print(f"Puntaje Sentimiento: {comentario_positivo['Puntaje Sentimiento']}")

    print("\nComentario más negativo:")
    print(f"Comentario: {comentario_negativo['Comentario']}")
    print(f"Puntaje Sentimiento: {comentario_negativo['Puntaje Sentimiento']}")

    # Guardar el resumen en un archivo de texto
    with open("informe_sentimientos.txt", "w", encoding="utf-8") as f:
        f.write("Resumen de Sentimientos:\n")
        f.write(conteo_sentimientos.to_string())
        f.write("\n\nEstadísticas descriptivas de los puntajes de sentimiento:\n")
        f.write(df["Puntaje Sentimiento"].describe().to_string())
        f.write("\n\nComentario más positivo:\n")
        f.write(f"Comentario: {comentario_positivo['Comentario']}\n")
        f.write(f"Puntaje Sentimiento: {comentario_positivo['Puntaje Sentimiento']}\n")
        f.write("\nComentario más negativo:\n")
        f.write(f"Comentario: {comentario_negativo['Comentario']}\n")

    print("\nInforme generado: 'informe_sentimientos.txt'")
    print("Gráfico guardado: 'grafico_sentimientos.png'")
else:
    print("\nNo se encontró ningún post que coincida exactamente con el enunciado proporcionado.")