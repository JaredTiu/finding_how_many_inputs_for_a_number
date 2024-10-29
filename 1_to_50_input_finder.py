#make a loop for user input 
while True:
    while True: 
        try: 
            age = int(input("input a number: "))
            if age < 0 or age > 50:
                raise
            break
        except: 
            print("Only add numbers from 1 to 50")
            
    retry = input("Do you want to input another number?: ")

    if retry == "no" or retry == "No" or retry == "No":
        break

#add definitions for valid age 

#get info to a  list 

#find a way to detect how many inputs for a number in that list 

#if they stop inputing print how many inputs 

