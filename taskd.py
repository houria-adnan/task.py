#The user enters the birthdays of, a and b, two people who were born on different days in the same year. Write Python code that prints a is younger if a's birthday comes before b's, and b is younger if b's birthday comes before a's.
print("Roll number 12")
person_a= int(input('Enter date of birth of A: '))
person_b= int(input('Enter date of birth of B: '))

if(person_a > person_b):
    print("Person A is elder than person B")

elif(person_b > person_a):
    print("Person B is elder than person A")
