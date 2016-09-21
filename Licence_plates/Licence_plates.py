#! /usr/bin/env python

import lp_modules

data = lp_modules.read_json("DB.json")
print "Witaj w programie i wybierz 1 lub 2"
choose = lp_modules.Choose()
find_using, value = lp_modules.Plate_or_city(choose)
lp_modules.show(data,find_using,value)


