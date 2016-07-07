#! /usr/bin/env python

#from nowymoduly import twojeliczbyfun, losowaneliczbyfun

import nowymoduly

 
twojeliczby = []
liczby = []
#wygrana =0
losowanie =[]


nick,obecne,gry = nowymoduly.ustawienia()
nazwa = nick + ".json"
    
while  True:

    losowanie = nowymoduly.czytaj_json(nazwa)
    
    if not losowanie:
        losowanie.append(gry)
        losowanie.append(obecne) 
        nowymoduly.zapisz_json(nazwa,losowanie)
             
    o = nowymoduly.rodzajdef()
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
    
    
    losowanie[1] = saldoo
    losowanie[0]=losowanie[0]+1
    nowymoduly.zapisz_json(nazwa,losowanie)
   

    z = nowymoduly.pytaniedofun()    
    
    if z =='n':
         break     
         
           
 
        
       
        

