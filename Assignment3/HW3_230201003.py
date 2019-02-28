#230201003
#-*- coding: utf-8 -*- 

myfile = ("contacts.txt")
def ShowMenu():
    Verification = False
    while Verification == False: #Keeps showing menu until valid input entered(verification=true)
        print "Main menu: "
        print "1. List all contacts"
        print "2. Find contact"
        print "3. Add contact"
        print "4. Remove contact"
        print "5. Save and quit"
        global Selection
        Selection = raw_input("Please enter option number :")
        if (Selection == "1") or (Selection == "2") or (Selection == "3") or (Selection == "4") or (Selection == "5"):
            Verification = True
        else :
            print "Invalid input. Please enter an input correctly!"
        Process()
def ListUp(): #Creates lists to keep changes
    global Name_list 
    Name_list = []
    global Number_list 
    Number_list = []
    infile = open(myfile,"r") # Opens file for reading
    a = infile.readline()
    while a != "":
        Name_list.append(a.split("#")[0]) # Adds name in name list without number
        Number_list.append(a.split("#")[1]) # Adds number in number list without name
        a = infile.readline()
    infile.close()

def Separation(): # Creates a list which has separated numbers to show numbers separately
    global Separated_list
    Separated_list = []
    for i in range(0,len(Number_list)): 
        Separated_list.append(str(Number_list[i]))
    for i in range(0,len(Separated_list)): 
        A =  (Separated_list[i])[0] + (Separated_list[i])[1] + (Separated_list[i])[2],(Separated_list[i])[3] + (Separated_list[i])[4] + (Separated_list[i])[5], (Separated_list[i])[6] + (Separated_list[i])[7], (Separated_list[i])[8] + (Separated_list[i])[9]
        Separated_list[i] = ' '.join(A)
def Search_name(x): # Searches name 
    global Found
    Found = False
    for i in range(0,len(Name_list)):
        if x.lower() == Name_list[i].lower(): #(case-insensitive)
            Found = True
            global Asked_index
            Asked_index = i
            break
        else :
            Found = False
def Process(): #Performs the action required.
    while Selection == "1" :
        Separation()
        for i in range(0,len(Name_list)):
            print Name_list[i], Separated_list[i]
        ShowMenu()
    while Selection == "2" :
        S_name = raw_input("Please enter a name : ")
        Separation()#Calls function to be able to show number separately
        Search_name(S_name.lower())#Calls function to search name
        if Found == True:
                print Name_list[Asked_index] + "'s phone number is",Separated_list[Asked_index]
                print "Submenu: "
                print "1. Edit name"
                print "2. Edit phone number"
                print "3. Continue"
                Sub_Selection = raw_input("Please enter option number :")
                if Sub_Selection == "1":
                    New_name = raw_input("Please enter a new name :")
                    Search_name(New_name.lower())
                    if Found == True:
                        print "This person already exists."
                        ShowMenu()
                    else :
                        Name_list[Asked_index] = New_name
                        print "Contact is updated."
                        ShowMenu()
                elif Sub_Selection == "2":
                    New_number = raw_input("Please enter a new phone number :")
                    if len(str(New_number)) == 10 and str(New_number).isdigit() == True:
                        Number_list[Asked_index] = str(New_number)
                        print "Contact is updated."
                        ShowMenu()
                    else :
                        print "This phone number is invalid."
                        ShowMenu()
                elif Sub_Selection == "3":
                    ShowMenu()
                else :
                    print "Invalid input is entered."
                    ShowMenu()
        else :
            print "No such contact exists."
            ShowMenu()
    while Selection == "3" :
        New_name2 = raw_input("Please enter a new name :")
        New_number2 = raw_input("Please enter a new phone number :")
        Search_name(New_name2.lower())#Calls function to search name
        if Found == True and len(str(New_number2)) != 10 :
            print "This person already exists and phone number is invalid."
            ShowMenu()
        elif Found ==True :
            if str(New_number2).isdigit() == True:
                print "This person already exists."
            else:
                print "This person already exists and phone number is invalid."
            ShowMenu()
        elif len(str(New_number2)) != 10:
            print "This phone number is invalid."
            ShowMenu()
        elif str(New_number2).isdigit() == False:
            print "This phone number is invalid."
        else :
            Name_list.append(New_name2)
            Number_list.append(str(New_number2)+"\n")
            print "New contact is added."
            ShowMenu()
    while Selection == "4":
        S_name2 = raw_input("Please enter the name :")
        Search_name(S_name2.lower())#Calls function to search name
        if Found == False :
            print "No such contact exists."
            ShowMenu()
        else:
            del Name_list[Asked_index]
            del Number_list[Asked_index]
            print "Contact is removed."
            ShowMenu()
    while Selection == "5":
        Write = open("contacts.txt","w")
        for i in range(0,len(Number_list)): #If there is no \n at the end of a number(For example, last line of the first version of contacts.txt), this code adds \n to pass new line
            if str(Number_list[i][-1]) == "\n":
                Abc128 = "Do nothing" #Pointless line
            else:
                Number_list[i] = str(Number_list[i])+"\n"
        for i in range(0,len(Name_list)):
            Write.write(Name_list[i]+"#"+str(Number_list[i]))
        Write.close()
        break
        quit()

ListUp()
ShowMenu()
