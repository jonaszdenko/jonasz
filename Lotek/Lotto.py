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
    set_value = 0
    #print main_data_from_json[0][0]

    if main_data_from_json: #jesli plik istnieje
	for i in main_data_from_json: # petla tyle razy ile pozycji w main_data
		if i[0] ==  nick:
        	 print "Rozegrane gry: " ,i[1]
         	 print "Saldo: " ,i[2] 
		 set_value = 1
    
    if set_value==0: 
	main_data_from_json.append(nick)
        main_data_from_json.append(game)
        main_data_from_json.append(current_ballance)
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
      
    
    ballance = lotto_modules.Ballance(main_data_from_json[2],win)
    data_from_json[2]= ballance
    print "Saldo:", ballance
    print "Gry: ", data_from_json[1]     

    if strike:
           print "trafione : ", strike
           print "\nIlosc trafien : ", len(strike)
    else:
           print "brak trafien!"
    
    
    
    lotto_modules.Add_json(name_of_json,main_data_from_json)
   
    print "Obecne saldo =", ballance
    again = lotto_modules.Question()    
    os.system('clear')
    
    
   
    if ballance <=0:
         print "Niestety nie mozesz grac dalej, bo przegrales hajs!!! Idz do roboty i wroc!"
         break     
    elif again =='n':
         break  
 
        
       
        

