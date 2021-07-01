

import sys
#Database info 
x = 0 #used as a variable for while loop
y = 0 #used as a variable for while loop
z = 0 #used as a variable for while loop
c = 0 #used as a variable for --group loop
e = 0 
g = 0 #Used as a variable for transaction loop
num_of_people = 1
currency = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05] #Different types of bills which are payable
currency_amounts = [] #Tallies up the amount of currencies needed respectively
non_decimal_currency = []
for items in currency: #Creates list without decimals
    if items < 1:
        non_decimal_currency.append(int(items*100))
    else:
        non_decimal_currency.append(int(items))
x = 0
popcorncost = [3.50, 5.00, 7.00]
popcornlist = []
movie_ticket_cost = [13, 13, 13, 15, 15, 15, 13, 13, 13, 15, 15, 15, 13, 13, 13, 15, 15, 15, 15]
movie_size = [18, 18, 18, 18, 18, 18, 68, 68, 68, 68, 68, 68, 21, 21, 21, 21, 21, 21, 21]
movie_times = ['1000','1300','1500','1730','1930','2145','1000','1215','1445','1745','2100','2320','1000','1130','1430','1700','1900','2100','2215']
movie_title = ['The Shining','Your Name',"Fate/Stay Night: Heaven's Feel - III. Spring Song",'The Night Is Short, Walk on Girl','The Truman Show','Genocidal Organ',"Jacob's Ladder",'Parasite','The Dark Knight','Blade Runner 2049','The Mist','Demon Slayer: Mugen Train','The Matrix','Inception','Shutter Island','Soul','Mrs. Brown','Peppa Pig: Festival of Fun','Titanic']
movie_rdate = ['1980','2016','2020','2017','1998','2017','1990','2019','2008','2017','2007','2020','1999','2010','2020','1997','2019','1997']
movie_duration = ['2h 26m','1h 52m','2h 0m','1h 32m','1h 47m','1hr 55m','1h 56m','2h 12m','2h 32min','2h 44m','2h 6m','1h59min','2h 16m','2h 42m','2h 19m','1hr 40m','1h 41min','1h 8min','3h 30min']
movie_fulldesc = ["The Shining. 1980. 2h 26m. 10:00. Room 1",
"Your Name. 2016. 1h 52m. 13:00. Room 1",
"Fate/Stay Night: Heaven's Feel - III. Spring Song. 2020. 2h 0m. 15:00. Room 1",
"The Night Is Short, Walk on Girl. 2017. 1h 32m. 17:30. Room 1",
"The Truman Show. 1998. 1h 47m. 19:30. Room 1",
"Genocidal Organ. 2017. 1hr 55m. 21:45. Room 1",
"Jacob's Ladder. 1990. 1h 56m. 10:00. Room 2",
"Parasite. 2019. 2h 12m. 12:15. Room 2",
"The Dark Knight. 2008. 2h 32min. 14:45. Room 2",
"Blade Runner 2049. 2017. 2h 44m. 17:45. Room 2",
"The Mist. 2007. 2h 6m. 21:00. Room 2",
"Demon Slayer: Mugen Train. 2020. 1h59min. 23:20. Room 2",
"The Matrix. 1999. 2h 16m. 10:00. Room 3",
"Inception. 2010. 2h 42m. 11:30. Room 3",
"Shutter Island. 2010. 2h 19m. 14:30. Room 3",
"Soul. 2020. 1hr 40m. 17:00. Room 3",
"Mrs. Brown. 1997. 1h 41min. 19:00. Room 3",
"Peppa Pig: Festival of Fun. 2019. 1h 8min. 21:00. Room 3",
"Titanic. 1997. 3h 30min. 22:15. Room 3"]


#First operation
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ Welcome to Pizzaz cinema ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

#Switch Errors on command line
try: 
    switch = sys.argv[1] #looks for arguments in the command line 
except IndexError: #If there is no switch argument it will print the bottom line
    print('Usage: python3 MovieTicketOrder.py [ --show <timenow> | --book | --group ]')
    exit()
if len(sys.argv) > 3: #If too many arguments then it will print error messege
    print("Sorry. This program does not recognise the switch options entered.")
    print("Bye")
    exit()

#Switch --show operation
elif switch == '--show': 
    if len(sys.argv) == 2: #No time is inputted as there are only two cmd args
        print("Sorry. This program does not recognise the switch options.")
        print("Bye")
        exit()
    
    elif len(sys.argv) != 2:
        try:
            time = sys.argv[2] #Takes the 3rd cmd arg and attributes it to time variable
            nocolontime = time.replace(':','') #Removing colon makes it easier to compare inputs and movie_times list
            time_char = len(nocolontime)
            if not len(nocolontime) == 4: #If the time inputted is not 4 characters, quites program
                exit()
            hours = nocolontime[0] + nocolontime[1] #Takes the first 2 characters of nocolontime to find the hours
            minutes = nocolontime[2] + nocolontime[3] #Likewise using last 2 characters finds minutes
            if int(hours) >= 24 or int(hours) < 0: #Sets parameters for what hours can be within
                exit()
            if int(minutes) > 59 or int(minutes) < 0: #Sets parameters for what minutes can be within
                exit()

            try:
                nocolontime = int(nocolontime) #Converts nocolontime string into int and back
                nocolontime = str(nocolontime)
            except: #If nocolontime could not be changed to an int, then the cmd is invalid and will exit
                exit()

            movies = [] #Empty list for tracking movies
            indextracker = -1 #Have to use a index tracker since using the list method doesn't work as indexing will give same location if there are duplicates
            for i in movie_times: #parses through all items in movie_times
                indextracker += 1 #Adds 1 to the index tracker to change position
                if nocolontime <= i: #Determines whether the time the user inputted is before the time of movies
                    print(movie_fulldesc[indextracker]) #If the user inputted time is before then it will print the movie description
            print("")
            print("Bye.")

        except: #If errors occur on line 77 and time cannot be attributed to sys.argv[2], program exits
            print("Sorry. This program does not recognise the time format entered.")
            print("Bye")
            exit()

#--book operation

elif switch == "--book":

    chosenmovie = "" #Empty string
    if len(sys.argv) >= 3: #If too many cmds are inputted then error
        print("Sorry. This program does not recognise the switch options.")
        print("")
        print("Bye")
        exit()

    while x == 0: #Used as a looping variable
        movieinput = input("What is the name of the movie you want to watch? ")
        
        movieinput = movieinput.lower() #Makes the input lower-case 
        for movieitem in movie_title: #For all moviesitems in movie_title list, if the input matched the movieitems
            if movieinput == movieitem.lower(): #It would break the loop 
                chosenmovie = movieitem
                x += 1
                break
            elif movieinput == "fate/stay night: heaven's feel - iii": #Alternative name for movie
                chosenmovie = "fate/stay night: heaven's feel - iii"
                x+=1
                break
            else:
                x = 0

        while x == 0: #if program cannot find movie, it will print message to retry
            option = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ")
            option = option.lower()
            if option == 'y': #Different options on either Y/N
                break
            elif option == 'n':
                print("Bye.")
                exit()
            
    popcornpayable = 0 #This is total cost payable for popcorn
    print("")
    while y == 0: #Looping variable
        x = 0
        popcorn = input("Would you like to order popcorn? Y/N ")
        popcorn = popcorn.upper()
        if popcorn == "Y":
            while x == 0: #looping variable
                popsize = input("You want popcorn. What size Small, Medium or Large? (S/M/L) ")
                popsize = popsize.upper()
                
                if popsize == "S":
                    popcornpayable += 3.50 #Adds to the variable
                    y += 1
                    break
                elif popsize == "M":
                    popcornpayable += 5.00
                    y += 1
                    break                

                elif popsize == "L":
                    popcornpayable += 7.00
                    y += 1
                    break

        elif popcorn == "N":
            y += 1
            break

        else:
            y == 0
    print("")
    print("The seat number for person 1 is #17")
    print("") #movie_title.index(chosenmovie) produces the position (integer) of the movie chosen in the list this index is passed through another list to determine price of movie
    total_cost = popcornpayable + movie_ticket_cost[movie_title.index(chosenmovie)] #Calculates cost from popcorn and movie ticket
    print("For 1 person, the initial cost is ${:.2f}".format(total_cost))

    if movie_ticket_cost[movie_title.index(chosenmovie)] == 13: #prints before or from based on movie price
        print(" Person 1: Ticket before 16:00    $13.00")
    elif movie_ticket_cost[movie_title.index(chosenmovie)] == 15:
        print(" Person 1: Ticket from 16:00      $15.00")
    
    if popcornpayable == 3.50:
        print(" Person 1: Small popcorn          $ 3.50")
    elif popcornpayable == 5.00:
        print(" Person 1: Medium popcorn         $ 5.00")
    elif popcornpayable == 7.00:
        print(" Person 1: Large popcorn          $ 7.00")
    else:
        pass
    print("")
    print(" No discounts applied             $ 0.00")
    print("")
    print("The final price is                ${:.2f}".format(total_cost))
    print("")

#Operation below will ask for money given and provide change
    while g == 0:
        moneygiven = float(input("Enter the amount paid: $")) 
        divisible_by_five = moneygiven*20 #Could not use %5 as it gives rounding errors
        change = total_cost - moneygiven
        formatted_change = "{:.2f}".format(change) 
        
        if (divisible_by_five).is_integer() == False: #Ensures that 5c is multiplied to an integer to see if it is divisble by 5
            print("The input given is not divisible by 5c. Enter a valid payment.")
        elif moneygiven < total_cost:
            print("The user is ${} short. Ask the user to pay the correct amount.".format(formatted_change))
        else:
            break

    change = change*-1
    formatted_change = "{:.2f}".format(change)
    print("Change: $" + str(formatted_change))

    for unit in currency:
        x = 0
        while change >= unit: #if the change amount is greater than the currency denomination
            change -= unit #minus the change with the denomination
            x += 1 #adding value to x changes the position on the list
        currency_amounts.append(x) #The amount of currency of that denomination is added to a separate list to track
        change = round(change, 2)

    y = 0 #Tracks position of currency_amounts list
    for x in currency_amounts:  #Parses through the currency_amount list and if the value is greater than 0 there is change to be given
        if x > 0:       #The following code prints out the change given and differentiates print options depending on the y value/position on list
            if y == 0:
                print(" $100: {}".format(x))
            elif y <= 3:
                print(" ${}: {}".format(non_decimal_currency[y], x))
            elif y <= 6:
                print(" $ {}: {}".format(non_decimal_currency[y], x))
            elif y <= 9:
                print(" {}c: {}".format(non_decimal_currency[y], x))
            elif y == 10:
                print("  {}c: {}".format(non_decimal_currency[y], x)) 

        y += 1
            

    print("\nBye.")
        


            

#Switch Group operation
elif switch == "--group":

    while x == 0: #Variable x is used as a looping variable
        movieinput = input("What is the name of the movie you want to watch? ")
        
        movieinput = movieinput.lower()
        for movieitem in movie_title:
            if movieinput == movieitem.lower():
                chosenmovie = movieitem
                x += 1
                break
            elif movieinput == "fate/stay night: heaven's feel - iii":
                chosenmovie = "fate/stay night: heaven's feel - iii"
                x+=1
                break
            else:
                x = 0

        while x == 0: #Used as a loopig variable
            option = input("Sorry, we could not find that movie. Enter Y to try again or N to quit. ")
            option = option.lower()
            if option == 'y':
                break
            elif option == 'n':
                print("\nBye.")
                exit()

    print("")
    while e == 0: #Looping variable
        try:
            num_of_people = int(input("How many persons will you like to book for? "))
            if num_of_people <= 1:
                f = 0 #Variable used for initiating next while loop
            else:
                f = 1 #Stops next while loop from occuring
                e = 1 #Ends current loop
        
        except:
           f = 0 #Any errors will cause the question to be asked again
        
        while f == 0: #looping variable
            YorN = input("Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ")
            YorN = YorN.upper()
            if YorN == "Y":
                f = 1
                pass
            elif YorN =="N":
                print("\nBye")
                exit()
            else:
                pass
        
        if num_of_people > movie_size[movie_title.index(chosenmovie)]: #if persons inputted is greater than room size
            e = 0
            while True:
                option = input("Sorry, we do not have enough space to hold {} people in the theater room of {} seats. Enter Y to try a different movie name or N to quit.".format(num_of_people, movie_size[movie_title.index(chosenmovie)]))
                option = option.lower()
                if option == 'y':
                    break
                elif option == 'n':
                    print("\nBye.")
                    exit()
    popcorntracker = 0
    print("")
    for z in range (1, num_of_people + 1): #Asks the following block to everyone 
        x = 0
        popcorn = input("For person {}, would you like to order popcorn? Y/N ".format(z))
        popcorn = popcorn.upper() #Makes all inputs uppercase 
        if popcorn == "Y":
            popsize = input("Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) ".format(z))
            popsize = popsize.upper()
            
            if popsize == "S":
                popcornlist.append(3.50) #Adds popcorn item price to list 
                y += 1
                x += 1
                popcorntracker += 1
                
    
            elif popsize == "M":
                popcornlist.append(5.00)
                popcorntracker += 1
                y += 1
                        

            elif popsize == "L":
                popcornlist.append(7.00)
                y += 1
                popcorntracker += 1

        elif popcorn == "N":
            popcornlist.append(0.00)
        
        else:
            popcornlist.append(0.00)
    
    print("")
    seat = 1
    for z in range (1, num_of_people + 1): #prints the seating number based off of 1+2n
        print("The seat number for person {} is #{}".format(z, seat))
        seat += 2

    # Cost
    popcornsum = sum(popcornlist) #adds up all prices of popcorn
    movie_ticket_cost_sum = movie_ticket_cost[movie_title.index(chosenmovie)]*num_of_people #Multiplies movie cost with no.ppl
    total_cost = popcornsum + movie_ticket_cost_sum #Adds popcorn costs and ticket costs
    formatted_total_cost = "{:.2f}".format(total_cost) #Makes it 2dp

    print("")
    print("For {} persons, the initial cost is ${}".format(num_of_people, formatted_total_cost))

    for z in range (1, num_of_people + 1): #Prints line for each person
        if movie_ticket_cost[movie_title.index(chosenmovie)] == 13:
            print(" Person {}: Ticket before 16:00    $13.00".format(z))
        elif movie_ticket_cost[movie_title.index(chosenmovie)] == 15:
            print(" Person {}: Ticket from 16:00      $15.00".format(z))
        
        if popcornlist[z-1] == 3.50: #prints popcorn size after ticket price depending on size. Parses through popcornlist 
            print(" Person {}: Small popcorn          $ 3.50".format(z))
        elif popcornlist[z-1] == 5.00:
            print(" Person {}: Medium popcorn         $ 5.00".format(z))
        elif popcornlist[z-1] == 7.00:
            print(" Person {}: Large popcorn          $ 7.00".format(z))

    print("")
    if total_cost > 100: #if over $100, discounts to popcorn is 20% and movie is 10%
        popcorndiscount = popcornsum * 0.2
        movieticketdiscount = movie_ticket_cost_sum * 0.1
        formatted_popcorndiscount = "{:.2f}".format(popcorndiscount) #formats it to 2dp
        formatted_movieticketdiscount = "{:.2f}".format(movieticketdiscount)

        print(" Discount applied tickets x{}     -$ {}".format(num_of_people, formatted_movieticketdiscount))
        print(" Discount applied popcorn x{}     -$ {}".format(popcorntracker, formatted_popcorndiscount))

    else: #if not over $100, no discounts :(
        print(" No discounts applied             $ 0.00")
        popcorndiscount = 0
        movieticketdiscount = 0
    
    print("")

    total_cost = total_cost - popcorndiscount - movieticketdiscount
    formatted_total_cost = "{:.2f}".format(total_cost) #calculates total cost after discount

    print("The final price is                ${}".format(formatted_total_cost))
    print("")
  ##  
###This section is very similar to the one used in the --book section. More in-depth comments will be there
  ##
    while g == 0: #looping variable
        moneygiven = float(input("Enter the amount paid: $"))
        divisible_by_five = moneygiven*20 #multiply by 20 to get a full integer
        change = total_cost - moneygiven #calculates change
        formatted_change = "{:.2f}".format(change) 
        
        if (divisible_by_five).is_integer() == False: #same function/code as previously seen
            print("The input given is not divisible by 5c. Enter a valid payment.")
        elif moneygiven < total_cost:
            print("The user is ${} short. Ask the user to pay the correct amount.".format(formatted_change))
        else:
            break

    change = change*-1 #Same functions as --book 
    formatted_change = "{:.2f}".format(change)
    print("Change: $" + str(formatted_change))

    for unit in currency:
        x = 0
        while change >= unit:
            change -= unit
            x += 1
        currency_amounts.append(x)
        change = round(change, 2)

    y = 0
    for x in currency_amounts: #Section is the same as the section above for individuals
        if x > 0: #Refer to --book section for info
            if y == 0:
                print(" $100: {}".format(x))
            elif y <= 3:
                print(" ${}: {}".format(non_decimal_currency[y], x))
            elif y <= 6:
                print(" $ {}: {}".format(non_decimal_currency[y], x))
            elif y <= 9:
                print(" {}c: {}".format(non_decimal_currency[y], x))
            elif y == 10:
                print("  {}c: {}".format(non_decimal_currency[y], x)) 

        y += 1
            

    print("\nBye.")

else:
    print("Sorry. This program does not recognise the switch options.")
    print("Bye")
    exit()

