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
"""sklearn es una biblioteca de Python ampliamente 
utilizada para Machine Learning. 
Proporciona herramientas simples y eficientes para realizar
 tareas de aprendizaje automático y minería de datos.

Naive Bayes Multinomial de la biblioteca scikit-learn.
 Este modelo es un algoritmo de clasificación supervisado 
 basado en el teorema de Bayes y es especialmente útil 
 para tareas de clasificación de texto, como el análisis de sentimientos.
"""

import praw
import pandas as pd
import os
import matplotlib.pyplot as plt
import textwrap
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer

# 1. Configurar la conexión con Reddit
reddit = praw.Reddit(
    client_id="4gitJskjt121GuCBhB2_7g",       # Reemplaza con tu Client ID
    client_secret="zyL2beX4J2-14O79HG_Re_IZZSAz_g",  # Reemplaza con tu Client Secret
    user_agent="AnalisisSentimientoParaClase"  # Nombre de tu aplicación
)

# 2. Cargar un dataset de ejemplo para entrenar el modelo
# Puedes usar un dataset público o crear uno propio
# Aquí usamos un dataset ficticio como ejemplo
data = {
    "Texto": [
        "Me encanta este producto, es increíble",
        "No me gusta, es terrible",
        "Es un producto aceptable, nada especial",
        "¡Es fantástico! Muy recomendado",
        "No lo recomiendo, es muy malo"
    ],
    "Sentimiento": ["Positivo", "Negativo", "Neutral", "Positivo", "Negativo"]
}
df = pd.DataFrame(data)

# 3. Preprocesar los datos
# Lista de palabras vacías en español
stop_words_es = [
    "yo", "tú", "él", "ella", "nosotros", "vosotros", "ellos", "ellas",
    "un", "una", "unos", "unas", "el", "la", "los", "las", "de", "del",
    "que", "y", "o", "a", "en", "por", "para", "con", "sin", "sobre",
    "al", "lo", "como", "más", "muy", "pero", "ya", "sí", "no", "este",
    "esta", "estos", "estas", "eso", "esa", "esos", "esas", "mi", "tu",
    "su", "nuestro", "vuestro", "sus", "me", "te", "se", "nos", "os"
]

# Crear el vectorizador con palabras vacías en español
"""Preprocesamiento:
Se utiliza CountVectorizer para convertir los textos en una representación numérica (Bag of Words).
Se eliminan palabras vacías en español utilizando una lista personalizada (stop_words_es)."""
vectorizer = CountVectorizer(stop_words=stop_words_es)
X = vectorizer.fit_transform(df["Texto"])  # Matriz de características
y = df["Sentimiento"]  # Etiquetas

# 4. Dividir los datos en entrenamiento y prueba
"""División de datos:
Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar el modelo."""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenamiento del modelo:

"""Se entrena el modelo Naive Bayes con los datos de entrenamiento."""
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Evaluar el modelo
"""Se evalúa el modelo con los datos de prueba y se imprime un reporte de clasificación."""
y_pred = model.predict(X_test)
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))
print(f"Precisión: {accuracy_score(y_test, y_pred)}")

# 7. Solicitar el enunciado exacto al usuario
query = input("Digite el enunciado exacto que desea buscar en Reddit: ")

# 8. Buscar publicaciones relacionadas con el enunciado exacto
subreddit = reddit.subreddit("all")  # Puedes especificar un subreddit, como "Colombia"
posts = subreddit.search(query, limit=100)

# 9. Analizar los comentarios del post
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

    # Analizar los comentarios
    comentarios_data = []
    post_encontrado.comments.replace_more(limit=None)  # Cargar todos los comentarios
    for comentario in post_encontrado.comments.list():
        """Los comentarios de la publicación encontrada se preprocesan con el mismo CountVectorizer utilizado en el entrenamiento.
           El modelo predice el sentimiento de cada comentario."""
        comentario_preprocesado = vectorizer.transform([comentario.body])  # Preprocesar el comentario
        sentimiento_predicho = model.predict(comentario_preprocesado)[0]  # Predecir el sentimiento
        comentarios_data.append({
            "Comentario": comentario.body,
            "Upvotes": comentario.score,
            "Sentimiento": sentimiento_predicho
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
else:
    print("\nNo se encontró ningún post que coincida exactamente con el enunciado proporcionado.")