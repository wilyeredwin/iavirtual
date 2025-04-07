from classifier import SentimentClassifier  # Use relative import if classifier.py is in the same package

clf = SentimentClassifier()

x = "El producto es excelente, me encanta!"
y = "El producto es malo, no me gusta."
z = "El producto es regular, no está mal pero tampoco es bueno."

sentimiento = clf.predict(x)
print(f"El sentimiento de la frase '{x}' es: {sentimiento}")
sentimiento = clf.predict(y)
print(f"El sentimiento de la frase '{y}' es: {sentimiento}")
sentimiento = clf.predict(z)
print(f"El sentimiento de la frase '{z}' es: {sentimiento}")
sentimiento = clf.predict("El producto es muy bueno")
