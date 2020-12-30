
print("roll number = Ic-012")
#Vowels count
#consonants count
string = input("Enter a string: " ). strip().replace(" ","")
vowelc= 0
consonantc= 0

for i in range(0,len(string)):
    if (string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u"):
        vowelc += 1 



    else:
        consonantc += 1

print("vowels" ,vowelc)
print("consonant",consonantc)
print(len(string))



