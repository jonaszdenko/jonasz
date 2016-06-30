#! /usr/bin/env python



import random

twojeliczby = []
liczby = []



for i in range(6):
    
  

  while True:
    
    j=0
   
    try: 
        twojaliczba = int(raw_input("Podaj twoja liczbe " + str(i+1) + " : "))

        if twojaliczba < 1 or twojaliczba > 49:
           print "Bledne dane!!!"
           j=1
           

        else:
          if twojeliczby.count(twojaliczba)==0:
              twojeliczby.append(twojaliczba)
          else:
              print "Ta liczba juz byla!"
              j=1

          
    except:
         print "zla podana wartosc"
         j=1

    if j==0:
      break

print "Twoje liczby", twojeliczby

for i in range(6):

       liczba = random.randint(1,49)
       if liczby.count(liczba)==0:
          liczby.append(liczba)      
    

print "wylosowane liczby : ", liczby


trafione = set(twojeliczby) & set(liczby)

if trafione:
       print "trafione : ", trafione
       print "\nIlosc trafien : ", len(trafione)
else:
       print "brak trafien!"
   

