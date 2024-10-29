#get info to a  list
list_of_numbers = []
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

    if retry == "no" or retry == "No" or retry == "No":
        break

#get info to a  list 

#find a way to detect how many inputs for a number in that list 

#if they stop inputing print how many inputs 

