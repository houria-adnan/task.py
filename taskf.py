
number= int(input("enter a value:"))
oddnumbers=0
for i in range(1,number+1):
    if(i%2 != 0):
        oddnumbers += i 
        print("oddnumber is:",i)
print("sun of oddnumbers are:", oddnumbers)

    