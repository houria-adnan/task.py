#Write a Python program to check whether a number is completely divisible by another
#number. Accept two integer values from the user.
 
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: ')) 

# % gives remainder


if(num1 % num2 == 0):
     print('First number is divisible by second number')

if(num1 % num2 != 0):
    print('First number is not divisible by second number')
