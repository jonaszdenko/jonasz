#! /usr/bin/env python

import random

#funkcja w ktorej podajemy nasze liczby. Szesc liczb w petli for.
#Kolejno obsulga wyjatkow (while: co ma robic, try:jesli jakis wyjatek na wejsciu to co robic. Kolejno jesli liczba ze zlego zakresu i kiedy liczba sie powtarza
def twojeliczbyfun():

    twojeliczby =[]
 

    for i in range(6):
    
      while True:
    
        j=0#jesli to znaczy ze udalo sie dodac liczbe, j zmienia swoj stan jesli cos jest nie tak ( dziala to na zasadzie do...while z tym. 
   
        try: 
            twojaliczba = int(raw_input("Podaj twoja liczbe " + str(i+1) + " : "))

            if twojaliczba < 1 or twojaliczba > 49:
               print "Bledne dane!!!"
               j=1
           

            else:
              if twojeliczby.count(twojaliczba)==0:#liczy ilosc liczb w zbiorze liczby jesli jest ich 0 to idzie dalej
                  twojeliczby.append(twojaliczba)#dodaeje do zbioru
              else:
                  print "Ta liczba juz byla!"
                  j=1

          
        except:
             print "zla podana wartosc"
             j=1

        if j==0:
          break

    return(twojeliczby)




def losowaneliczbyfun():
 
    losowane = []

    for i in range(6):
        
       while True:
            
           j=0

           liczba = random.randint(1,49)
           if losowane.count(liczba)==0:
              losowane.append(liczba)      
           else:
            j=1
          
           if j==0:
              break

        

       
    return(losowane)
