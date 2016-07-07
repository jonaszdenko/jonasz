#! /usr/bin/env python

#from nowymoduly import twojeliczbyfun, losowaneliczbyfun

import nowymoduly

 
twojeliczby = []
liczby = []
obecne =30;
wygrana =0;

nick,obecne,gry = nowymoduly.ustawiienia()
nazwa = nick + ".json"
    
while  True:

    losowanie = nowymoduly.czytaj_json(nazwa)
        
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
      
    
    saldoo = nowymoduly.saldo(obecne,wygrana)
    obecne = saldoo
    print "Saldo:", saldoo
      

    if trafione:
           print "trafione : ", trafione
           print "\nIlosc trafien : ", len(trafione)
    else:
           print "brak trafien!"
   
      

    z = nowymoduly.pytaniedofun()    
    
    if z =='n':
         break     
         
           
 
        
       
        

