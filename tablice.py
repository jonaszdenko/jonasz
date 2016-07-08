#! /usr/bin/env python
import nowymoduly

"""plik = "ta.json"

lista = []

lista.append({
    "rejest": 'RSA',
    "woj": "Podkarpackie",
    "miasto": "Sanok"
     })

lista.append({
    "rejest": "KT",
    "woj": "Malopolskie",
    "miasto": "Tarnow"
     })
nowymoduly.zapisz_json(plik,lista)
"""

lista = nowymoduly.czytaj_json("tabl.json")

o = raw_input("Daj rejestracje ")

for i in range(397):
  if lista[i]["rejestr"] == o:
    print lista[i]["miasto"]
    break
