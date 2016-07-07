#! /usr/bin/env python

#from nowymoduly import twojeliczbyfun, losowaneliczbyfun

import nowymoduly
import os
 
twojeliczby = []
liczby = []
#wygrana =0
losowanie =[]


nick,obecne,gry = nowymoduly.ustawienia()
nazwa = "folder/" + nick + ".json"
print "Witaj w grze" ,nick
   
while  True:

    losowanie = nowymoduly.czytaj_json(nazwa)
    if losowanie:
         print "Rozegrane gry: " ,losowanie[0]
         print "Saldo: " ,losowanie[1]     
    if not losowanie:
        losowanie.append(gry)
        losowanie.append(obecne) 
        nowymoduly.zapisz_json(nazwa,losowanie)
             
    o = nowymoduly.rodzajdef()
    os.system('CLS')
   

    if o ==1:
        twojeliczby=nowymoduly.losowaneliczbyfun()
    else:
        twojeliczby = nowymoduly.twojeliczbyfun()

    liczby = nowymoduly.losowaneliczbyfun()
    
    print "Twoje liczby", twojeliczby
    print "wylosowane liczby : ", liczby
    
     
    trafione = set(twojeliczby) & set(liczby)
    wygrana = nowymoduly.wygrane(len(trafione))
      
    
    saldoo = nowymoduly.saldo(losowanie[1],wygrana)
    losowanie[1]= saldoo
    print "Saldo:", saldoo
    print "Gry: ", losowanie[0]     

    if trafione:
           print "trafione : ", trafione
           print "\nIlosc trafien : ", len(trafione)
    else:
           print "brak trafien!"
    
    
    
    losowanie[0]=losowanie[0]+1
    nowymoduly.zapisz_json(nazwa,losowanie)
   
    print "Obecne saldo =", saldoo
    z = nowymoduly.pytaniedofun()    
    os.system('CLS')
    
    
   
    if saldoo <=0:
         print "Niestety nie mozesz grac dalej, bo przegrales hajs!!! Idz do roboty i wroc!"
         break     
    elif z =='n':
         break  
 
        
       
        

