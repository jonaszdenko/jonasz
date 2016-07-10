#! /usr/bin/env python

import nowymoduly
import tablice_mod

lista = nowymoduly.czytaj_json("tabl.json")



print "Witaj w programie i wybierz 1 lub 2"

wybor = tablice_mod.wybor()
po_czym, input = tablice_mod.rej_czy_miasto(wybor)

tablice_mod.wyswietl(lista,po_czym,input)


"""o = raw_input("Daj rejestracje ")


for i in range(397):
  if lista[i]["rejestr"] == o.upper():
    
    print "Rejestracja : ", lista[i]["rejest"]
    print "Wojewodztwo : ", lista[i]["woje"]

    d =len(0)
    if d==2: 
       print "Miasto : ", lista[i]["miasto"]
    else:
       print "Powiat : ", lista[i]["miasto"]
    break
"""
