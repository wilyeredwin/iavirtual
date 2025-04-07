# Codigo para presentación de tema Técnicas de Machine Learning y Cuándo Usarlas
#  Análisis de sentimientos en redes sociales. SALA 5 
# Autorres : Grupo 12  Escrito WE-FERIA

# https://developer.x.com/en/portal/projects/1908614616055209984/apps/30518244/keys
# Obtén tu Bearer Token:
# Ve al Twitter Developer Portal.
# Selecciona tu proyecto y aplicación.
# Copia el Bearer Token.
import tweepy
import pandas as pd

# Configura el Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOSr0QEAAAAAEOvE4Lz1glABpSx0GzkFGvLSDS8%3DpHAu1FJbq6cmcY7Tq2fGbnG1okh2afShmZgVSCEWLQkMaOYJ9w"

# Autenticación
client = tweepy.Client(bearer_token=bearer_token)

# Buscar tweets
query = "Álvaro Uribe proceso judicial lang:es"
response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "text", "author_id"])

# Procesar los tweets
tweets = response.data
data = [[tweet.created_at, tweet.author_id, tweet.text] for tweet in tweets]

# Guardar en un DataFrame
df = pd.DataFrame(data, columns=["Fecha", "Usuario", "Contenido"])

# Guardar en un archivo CSV
df.to_csv("tweets_alvaro_uribe.csv", index=False, encoding="utf-8")
print("Tweets guardados en tweets_alvaro_uribe.csv")