#! /usr/bin/env python



import random

twojeliczby = []
liczby =[]


for i in range(6):
    
    twojaliczba = int(raw_input("Podaj twoja liczbe " + str(i+1) + " : "))
    if twojaliczba > 1 and twojaliczba <49:
        if twojeliczby.count(twojaliczba)==0:
            twojeliczby.append(twojaliczba)
        else: 
            print "Ta liczba juz byla!! ( Podaj inna)"
           # i = i + 1
    else:
         print "Zly zakres!!!"
         # i = i + 1

print "Twoje liczby", twojeliczby


for i in range(6):

    liczba = random.randint(1,49)
    if liczby.count(liczba)==0:
        liczby.append(liczba)


print "wylosowane liczby : ", liczby

