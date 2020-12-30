#question3
#)Write a Python program that uses an if statement to find the smallest of three given integers. (The user should enter the three numbers).
print("Roll number 12")
num_1= int(input('Enter a num_1: '))
num_2= int(input('Enter a num_2: '))
num_3= int(input('Enter a num_3: '))
if num_1 < num_2 and num_1 < num_3:
    smallest = num_1
if num_2 < num_1 and num_2 < num_3:
    smallest = num_2
if num_3 < num_1 and num_3 < num_2:
    smallest = num_3 
    print(smallest, "is the smallest of three numbers")
    
