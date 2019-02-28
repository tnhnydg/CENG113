#Student ID : 230201003 / " Tunahan Yadigarbigun "
filename = "employee.txt"
infile = open(filename,"r")
Inq_name = raw_input("Please enter the name to search:") #Asks for name
Ins_name = Inq_name.lower() #For case insensitivity
if Ins_name != "quit" :
    while Ins_name != "quit":
        line = infile.readline()
        Line_list = line.split(" ")
        if Line_list[0].lower() == Ins_name :  #For case insensitivity
            Base_s = int(Line_list[1]) # Base salary
            Amount_s = int(Line_list[2]) # Amount of sale
            if Amount_s >= 0 and Amount_s < 5 :
                Base_s = Base_s
                print Line_list[0] + "'s salary is " + str(Base_s)
            elif Amount_s >= 5 and Amount_s < 10 :
                Base_s = Base_s + 15
                print Line_list[0] + "'s salary is " + str(Base_s)
            elif Amount_s >= 10 and Amount_s < 25 :
                Base_s = Base_s + 25
                print Line_list[0] + "'s salary is " + str(Base_s)
            elif Amount_s >= 25 :
                Base_s = Base_s + 50
                print Line_list[0] + "'s salary is " + str(Base_s)
            else :
                print "False Value."
            
        else :
            print "The name couldn't find."
            
        Inq_name = raw_input("Please enter the name to search:")
        Ins_name = Inq_name.lower()
        
else :
    c = "User wanted to quit." # Meaningless line, just finishes without any prints.