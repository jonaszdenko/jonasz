#! /usr/bin/env python

import nowymoduly

lista = nowymoduly.czytaj_json("tabl.json")

o = raw_input("Daj rejestracje ")
d = len(o)

for i in range(397):
  if lista[i]["rejestr"] == o.upper():

    print "Wojewodztwo : ", lista[i]["woje"]
    if d==2: 
       print "Miasto : ", lista[i]["miasto"]
    else:
       print "Powiat : ", lista[i]["miasto"]
    break
