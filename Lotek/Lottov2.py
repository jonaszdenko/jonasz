#! /usr/bin/env python


import lotto_modules
import os

######################################## 
your_numbers = []
random_numbers = []
main_data_from_json =[]
data_from_json =[]



nick, current_ballance, game = lotto_modules.Settings()
name_of_json = "data_to_lotto.json"
print "Witaj w grze", nick
   
while  True:

    main_data_from_json = lotto_modules.Read_json(name_of_json)
    set = 0
    
    if main_data_from_json:
	for i in main_data_from_json:
		if data_from_json[0] == nick:
        	 print "Rozegrane gry: " ,data_from_json[1]
         	 print "Saldo: " ,data_from_json[2] 
		 set = 1    
    if set==0: 
	data_from_json.append(nick)
        data_from_json.append(game)
        data_from_json.append(current_ballance)
	main_data_from_json.append(data_from_json) 
        lotto_modules.Add_json(name_of_json,main_data_from_json)
             
    value_1_or_2 = lotto_modules.Choose()
    os.system('clear')
   

    if value_1_or_2 ==1:
        your_numbers = lotto_modules.RandomNumbers()
    else:
        your_numbers = lotto_modules.YourNumbers()

    random_numbers = lotto_modules.RandomNumbers()
    
    print "Twoje liczby", your_numbers
    print "wylosowane liczby : ", random_numbers
    
     
    strike = set(your_numbers) & set(random_numbers)
    win = lotto_modules.Win(len(strike))
      
    
    ballance = lotto_modules.Ballance(data_from_json[2],win)
    data_from_json[2]= ballance
    print "Saldo:", ballance
    print "Gry: ", data_from_json[1]     

    if strike:
           print "trafione : ", strike
           print "\nIlosc trafien : ", len(strike)
    else:
           print "brak trafien!"
    
    
    
    data_from_json[1]=data_from_json[1]+1
    lotto_modules.Add_json(name_of_json,data_from_json)
   
    print "Obecne saldo =", ballance
    again = lotto_modules.Question()    
    os.system('clear')
    
    
   
    if ballance <=0:
         print "Niestety nie mozesz grac dalej, bo przegrales hajs!!! Idz do roboty i wroc!"
         break     
    elif again =='n':
         break  
 
        
       
        

