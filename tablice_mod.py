#! /usr/bin/env python

def wybor():
    
    while True:
      wybor = int(raw_input("Podaj Twoj wybor :"))
      if wybor == 1 or wybor ==2:
         break
      else:
         print "Zla wartosc! Jeszcze raz"

    return wybor



def rej_czy_miasto(wybor):
   if wybor == 1:
       po_czym = "rejestr"
       o = raw_input("Podaj rejestracje :")
   elif wybor ==2:
       po_czym = "miasto"
       o = raw_input("Podaj miasto :")
   return(po_czym,o)

def wyswietl(lista,po_czym,o):
   
 for i in range(397):

  

  if lista[i][po_czym][:3].upper()==o[:3].upper():

    print "Rejestracja : ", lista[i]["rejestr"]
    print "Wojewodztwo : ", lista[i]["woje"]

    d =len(o)
    if d==2:
       print "Miasto : ", lista[i]["miasto"]
    else:
       print "Powiat : ", lista[i]["miasto"]
    


