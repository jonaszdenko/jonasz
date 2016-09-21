#! /usr/bin/env python

import os
import json

# Mozna wybrac dwie opcje wyszukiwania.
# Funkcje w while ( dopuki nie wybierzemy 1 lub 2 bedzie dzialac). Zwraca wartosc 1 lub 2.

# MOZNA DODAC OBSLUGE WYJATKOW


def Choose():
    
    while True:
      choose = int(raw_input("Podaj Twoj wybor :"))
      if choose==1 or choose==2:
         break
      else:
         print "Zla wartosc! Jeszcze raz"

    return choose


#################################################################################


#Funkcja przyjmuje rejestracje lub miasto, ktore chcemy wyszukac
#Funkcja przyjmuje wybor z funkcji Choose. Zwraca informacje czy wyszukujemy miasta czy rejestracji (find_using) oraz podana przez nas nazwe (value1)

def Plate_or_city(choose):
   
   if choose==1:
       find_using = "plate"
       value = raw_input("Podaj rejestracje :")
   elif choose==2:
       find_using = "city"
       value = raw_input("Podaj miasto :")

   return(find_using,value)

#################################################################################


#Funkcja wyszukuje i wyswietla zadane wyrazenie



def show(DB_plates,find_using,value):
    
 for from_DB in DB_plates:

  if from_DB[find_using][:3].upper()==value[:3].upper(): # wyciagamy ity element listy (i), nastepnie porownujemy pierwsze trzy znaki wartosc z kluczem (find_user) do podanej wartosci (value).

    print "Rejestracja : ", from_DB["plate"]
    print "Wojewodztwo : ", from_DB["country"]

    length =len(value)# jesli rejestracja ma 2 znaki to jest to miasto a jak 3 to powiat.

    if length==2:
       print "Miasto : ", from_DB["city"]
    else:
       print "Powiat : ", from_DB["city"]
    


##################################################################################


def read_json(file_name):

    data = []

    if os.path.isfile(file_name):
        with open(file_name, "r") as forward_obj:
            data = json.load(forward_obj)

    return data



