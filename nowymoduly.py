#! /usr/bin/env python

import random

def twojeliczby():

 
	

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

    return(twojeliczby)




