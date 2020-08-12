# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:47:58 2020

@author: Renzo
"""
"""Descripción:
    El programa toma la frase y analiza las palabras, cada una evoca sentimientos
    por lo que el resultado final es un valor que va desde -1 a 1 pasando por 0
    siendo -1 un sentimiento negativo, 0 neutral y 1 positivo respectivamente.
    
    desde cmd comando pip install nltk
    luego abrir desde cmd python
    import nltk
    nltk.download()
    - abrirá una ventana en donde se puede descargar el contenido de la libreria.
    - dar en all download o solo vader_lexicon para el caso particular de este ejercicio
    
    """


#IMPORTADO DE LIBRERIAS

from nltk.sentiment.vader import SentimentIntensityAnalyzer

x1 = "It is a charming and beautiful product"
x2 = "It was a horrible experience!"
x3 = "I have nothing to say. Normal so far"

#instanciamos el analizador de sentimientos
sia = SentimentIntensityAnalyzer()

resultados = sia.polarity_scores(x2)

print(resultados)
#el resultado mostrado es un diccionario con un puntaje para cada sentimiento
# lo divide en neg, neu, pos y un valor llamado compound que va de -1 a 1
