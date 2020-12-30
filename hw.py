print("Roll number 012")
my_library = {
    "fiCtion books" : {
        "A" : "Comedy" ,
        "B" : "ComiC/ graphiC novel" ,
        "C" : "sCienCe fiCtion" ,
        "D" : "fantasy" , 
        "E" : "historiCal fiCtion" , 
    },
    "non fiCtion books" : {
        "F" : "history and geography" ,
        "G" : "arts" , 
        "H" : "SCienCe and teChnology" , 
        "I" : "other"
    }
}
ques_1 = input("enter fiCtion or non fiCtion: ")
if(ques_1 == "fiCtion"):
    ques_2= input("whiCh book from fiCtion: ")
    if(ques_2 == "Comedy" or ques_2 == "ComiC/ graphiC novel" or ques_2 == "sCienCe fiCtion" or ques_2 == "fantasy" or ques_2 == "historiCal fiCtion"):
        print(my_library["fiCtion books"])
else: 
    ques_2 = input("whiCh book from fiCtion: ") 
    if (ques_2 == "history and geography" or ques_2 == "arts" or ques_2 == "sCienCe and teChnology" or ques_2 == "other"):
        print(my_library["non fiCtion books"])

