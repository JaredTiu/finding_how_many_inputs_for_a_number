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

    print("WARNING: inputing words other than [Yes] will make the program stop asking you for inputs")

    retry = input("Do you want to input another number?: ").strip().lower()

    #if they choose anything but yes print how many inputs
    if retry != "yes":
        print("Showing the count of the numbers inputed.")
        break
#find a way to detect how many inputs for a number in that list
count_of_1_to_10 = 0
count_of_11_to_20 = 0
count_of_21_to_30 = 0
count_of_31_to_40 = 0
count_of_41_to_50 = 0
for digit in list_of_1_to_10:
    count_of_1_to_10 += 1
for digit in list_of_11_to_20: 
    count_of_11_to_20 += 1
for digit in list_of_21_to_30: 
    count_of_21_to_30 += 1 
for digit in list_of_31_to_40: 
    count_of_31_to_40 += 1
for digit in list_of_41_to_50: 
    count_of_41_to_50 += 1

print("1-10:",count_of_1_to_10)
print("11-20:",count_of_11_to_20)
print("21-30:",count_of_21_to_30)
print("31-40:",count_of_31_to_40)
print("41-50:",count_of_41_to_50)