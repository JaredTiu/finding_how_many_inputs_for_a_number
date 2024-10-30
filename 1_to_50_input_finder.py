#get info to a  list
list_of_1_to_10 = []
list_of_11_to_20 = []
list_of_21_to_30 = []
list_of_31_to_40 = []
list_of_41_to_50 = []

#make a loop for user input 
while True:
    while True: 
        try: 
            #add definitions for valid age 
            numbers = int(input("input a number: "))
            if numbers >= 1 and numbers <=10:
                list_of_1_to_10.append(numbers)
            elif numbers >= 11 and numbers <=20:
                list_of_11_to_20.append(numbers)
            elif numbers >= 21 and numbers <= 30: 
                list_of_21_to_30.append(numbers)
            elif numbers >= 31 and numbers <= 40:
                list_of_31_to_40.append(numbers)
            elif numbers >=40 and numbers <= 50:
                list_of_41_to_50.append(numbers)    
            else:
                raise
            break
        except: 
            print("Only add numbers from 1 to 50")
    retry = input("Do you want to input another number?: ")

    #if they stop inputing print how many inputs
    if retry == "no" or retry == "No" or retry == "No":
        #find a way to detect how many inputs for a number in that list

        break  

