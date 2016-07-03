#! /usr/bin/env python

#from nowymoduly import twojeliczbyfun, losowaneliczbyfun

import nowymoduly

twojeliczby = []
liczby = []


twojeliczby = nowymoduly.twojeliczbyfun()
liczby = nowymoduly.losowaneliczbyfun()

print "Twoje liczby", twojeliczby
print "wylosowane liczby : ", liczby


trafione = set(twojeliczby) & set(liczby)

if trafione:
       print "trafione : ", trafione
       print "\nIlosc trafien : ", len(trafione)
else:
       print "brak trafien!"
   

