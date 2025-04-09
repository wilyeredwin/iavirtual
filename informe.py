# pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo = "comentarios_analizados.csv"
df = pd.read_csv(archivo)

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
conteo_sentimientos.plot(kind="bar", color=["green", "red", "blue"])
plt.title("Distribución de Sentimientos en los Comentarios")
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