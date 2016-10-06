#! /usr/bin/env python

import random
import json
import os
import yaml

###################################################################

#funkcja w ktorej podajemy nasze liczby. Szesc liczb w petli for.
#Kolejno obsulga wyjatkow (while: co ma robic, try:jesli jakis wyjatek na wejsciu to co robic. Kolejno jesli liczba ze zlego zakresu i kiedy liczba sie powtarza

def YourNumbers():

    yournumbers =[]
 

    for i in range(6):
    
      while True:
        check=0#jesli 0 znaczy ze udalo sie dodac liczbe,  zmienia swoj stan jesli cos jest nie tak ( dziala to na zasadzie do...while z tym. 
   
	try: 
            yournumber = int(raw_input("Podaj twoja liczbe " + str(i+1) + " : "))

            if yournumber < 1 or yournumber > 49:
               print "Bledne dane!!!"
               check=1
          
            else:
              if yournumbers.count(yournumber)==0:#liczy ilosc liczb w zbiorze liczby jesli jest ich 0 to idzie dalej
                  yournumbers.append(yournumber)#dodaeje do zbioru
              else:
                  print "Ta liczba juz byla!"
                  check=1

          
	except:
             print "zla podana wartosc"
             check=1

        if check==0:
          break

    return(yournumbers)


##################################################################################

def RandomNumbers():
 
    randomnumbers = []

    for i in range(6):
        
       while True:
           check=0

           number = random.randint(1,49)
           if randomnumbers.count(number)==0:
              randomnumbers.append(number)      
           else:
            check=1
          
           if check==0:
              break
      
    return(randomnumbers)


##########################################################################

def Ballance(current,win):
    money = current - 3 + win
    return(money)


############################################################################

def Win(win):
    
    if win ==3:
       money = 10
       print "Wygrales ", money , " zl"

    elif win == 4:
       money =24
       print "Wygrales ", hajs ," zl"

    elif win == 5:
       money = 50000
       print "Wygrales ", hajs ," zl"

    elif win == 6:
       money = 6000000
       print "Wygrales ", money ," zl"
    else:
       money = 0
        

   
    return(money)



#############################################################################

def Question():
    
    while True:
        check=0
        
	question = raw_input("Grasz dalej? t/n")
 
        if question == 'n':
           break
        elif question != 't' and question !='n':
           print "Zly wybor wybierz t albo n"
           print "Wybierz inna wartosc tu"
           check=1 
        
	if check==0:
           break 

    return(question)


##############################################################################

def Choose():

    print "Chybil trafil [1], czy twoje liczby [2]?\n"
   
    while True:
        try:
            choose = int(raw_input("Podaj wybor: "))
            if choose ==1 or choose ==2:
               break
            else:
               print "Wartosc to 1 albo 2!!!"

        except:
              print "Zla wartosc!!!"

    return(choose)     

##############################################################################

def Settings():
    print "Witaj w grze lotto."
    nick = raw_input("Podaj nick: ")
    balance = 30
    game = 0
  
    return(nick, balance, game)

##################################################################################

def Read_json(file_name):
    data = []
    if os.path.isfile(file_name):
        with open(file_name, "r") as forward:
            data = yaml.load(forward)
    return data

###################################################################

def Add_json(file_name, data):
    with open(file_name, "w") as forward:
        json.dump(data, forward)



