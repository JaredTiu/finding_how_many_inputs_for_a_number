from collections import Counter

#get info to a  list
list_of_numbers = []
one_to_ten = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#make a loop for user input 
while True:
    while True: 
        try: 
            #add definitions for valid age 
            numbers = int(input("input a number: "))
            if numbers < 0 or numbers > 50:
                raise
            break
        except: 
            print("Only add numbers from 1 to 50")

        list_of_numbers = [numbers]


    retry = input("Do you want to input another number?: ")

    #if they stop inputing print how many inputs
    if retry == "no" or retry == "No" or retry == "No":
        #find a way to detect how many inputs for a number in that list
        count_1_to_10 = 0 
        for digit in list_of_numbers:
            if digit == 1:
                count_1_to_10 += 1
        
        print(count_1_to_10)

        break 

#find a way to detect how many inputs for a number in that list 
 

