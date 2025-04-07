#pip install scikit-learn
# pip install spanish-sentiment-analysis

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# para analizar mensajes corto por ejemplo de x
import pandas as pd


sid = SentimentIntensityAnalyzer()
df =pd.read_csv("sentimientos.csv")
df ["sentimiento"] = df["texto"].apply(lambda i: sid.polarity_scores(i)["compound"])
df.to_csv("sentimientosfinal.csv")

# Cargar el archivo CSV
df = pd.read_csv("sentimientosfinal.csv")

# Mostrar las primeras filas del archivo
print(df.head())



"""
x="Hola  me gustas como te presentas, es bello"
y="odio esas imagenes que puedo ver en tu pagina"
z="No tengo nada que opinar en tu publicación"
w="Es una experiencia que no causo impresion en mi"

resultados =sid .polarity_scores(x)
print("variable x",resultados)

resultados =sid .polarity_scores(y)
print("variable y",resultados)

resultados =sid .polarity_scores(z)
print("variable z",resultados)

resultados =sid .polarity_scores(w)
print("variable w",resultados)
"""




