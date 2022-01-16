import requests
import pandas as pd
from flask import Flask, render_template, url_for, request, jsonify

liste_variable = ['fixed acidity', 'volatile acidity', 'citric acid','residual sugar', 'chlorides', 'free sulfur dioxide','total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

idx = 0
Mon_input = []
for i in range(len(liste_variable)):
    Data = input("Quelle est la valeur de la caractéristique {} -> ".format(liste_variable[idx]))
    Mon_input.append(Data)
    idx+=1


mon_input =  Mon_input

response = requests.post("http://127.0.0.1:5000/quality", json={"quality": mon_input})
print(response.json())