def number_1_to_10 (numbers):
    for digit in numbers: 
        if digit >= 1 or digit <= 10:
            list_of_numbers_1_to_10[numbers]
    return True
def number_11_to_20 (numbers):
    for digit in numbers:
        if digit >= 11 or digit <= 20:
            list_of_numbers_11_to_20[numbers]
    return True     
def number_21_to_30 (numbers):
    for digit in numbers:
        if digit >= 21 or digit <= 30:
            list_of_numbers_21_to_30[numbers]
    return True
def number_31_to_40 (numbers):
    for digit in numbers:
        if digit >= 31 or digit <= 40:
            list_of_numbers_31_to_40[numbers]
    return True
def number_41_to_50 (numbers):
    for digit in numbers:
        if digit >= 41 or digit <= 50:
            list_of_numbers_41_to_50[numbers]
    return True

#get info to a  list
list_of_numbers_1_to_10 = []
list_of_numbers_11_to_20 = []
list_of_numbers_21_to_30 = []
list_of_numbers_31_to_40 = []
list_of_numbers_41_to_50 = []

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
        list_of_numbers_1_to_10 = [numbers]
        list_of_numbers_11_to_20 = [numbers]
        list_of_numbers_21_to_30 = [numbers]
        list_of_numbers_31_to_40 = [numbers]
        list_of_numbers_41_to_50 = [numbers]

    count = list_of_numbers_1_to_10.count(1)

    retry = input("Do you want to input another number?: ")

    #if they stop inputing print how many inputs
    if retry == "no" or retry == "No" or retry == "No":
        print([number_1_to_10] , count)
        break 

#find a way to detect how many inputs for a number in that list 
 

