#! /usr/bin/env python

#from nowymoduly import twojeliczbyfun, losowaneliczbyfun

import nowymoduly

 
twojeliczby = []
liczby = []
obecne =30;
wygrana =0;

    
        

while True:

    

    twojeliczby = nowymoduly.twojeliczbyfun()
    liczby = nowymoduly.losowaneliczbyfun()
    
    print "Twoje liczby", twojeliczby
    print "wylosowane liczby : ", liczby
    

    trafione = set(twojeliczby) & set(liczby)
    wygrana = nowymoduly.wygrane(len(trafione))
      
    
    saldoo = nowymoduly.saldo(obecne,wygrana)
    obecne = saldoo
    print "Saldo:", saldoo
      

    if trafione:
           print "trafione : ", trafione
           print "\nIlosc trafien : ", len(trafione)
    else:
           print "brak trafien!"
   
      

        

    zakoncz = raw_input("Grasz dalej? t/n")

    if zakoncz == 'n':
       break
    elif zakoncz == 't':
       continue
        
         
           
 
        
       
        

