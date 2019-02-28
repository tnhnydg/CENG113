# 230201003 / Tunahan Yadigarbigun

def Dict_keys(): #English words
    infile = open("dictionary.txt","r")
    list1 = infile.readlines()
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i].split("\t"))
    list3 = []
    for i in range(len(list2)):
        list3.append(list2[i][0])
    infile.close()   
    return list3

def Dict_values(): #Turkish translations
    infile = open("dictionary.txt","r")
    list1 = infile.readlines()
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i].split("\t"))
    list3 = []
    for i in range(len(list2)):
        list3.append(list2[i][1][:-1])
    infile.close()   
    return list3

def S_for_Alt(LookedUp,ToCompare): # Search for alternative word
    global Found1
    if abs(len(LookedUp) - len(ToCompare)) < 6 :
        if (LookedUp in ToCompare) or (ToCompare in LookedUp):
            return ToCompare
        else:
            return False
        
    else :
        return False
def Find_Cls(LookedUp,ToCompare): #Closest word
    def Distance(LookedUp,ToCompare):
        list1 = list(LookedUp)
        list2 = list(ToCompare)
        def Let_Diff(LookedUp,ToCompare):
            if len(LookedUp) >= len(ToCompare):
                for i in list2:
                    for j in list1:
                        if i == j:
                            list1.remove(list1[list1.index(j)])
                            list2.remove(list2[list2.index(i)])
                            break
            else:
                for i in list1:
                    for j in list2:
                        if i == j:
                            list1.remove(list1[list1.index(i)])
                            list2.remove(list2[list2.index(j)])
                            break
            return len(list1)+len(list2)
        def Len_Diff(LookedUp,ToCompare):
            z = abs(len(LookedUp)-len(ToCompare))
            if z == 0:
                z = 0.5
            return z
        def Coeff(LookedUp,ToCompare):
            Value = 1
            if LookedUp[0] == ToCompare[0]:
                Value = Value * 0.5
            if LookedUp[-1] == ToCompare[-1]:
                Value = Value * 0.5
            return Value
        return Let_Diff(LookedUp,ToCompare) * Len_Diff(LookedUp,ToCompare) * Coeff(LookedUp,ToCompare)
    Dis_list = []
    for i in Dict_keys():
        Dis_list.append(Distance(LookedUp,i))
    Index = Dis_list.index(min(Dis_list))
    return Dict_keys()[Index]
def S_Binary(LookedUp,List): # Binary Search
    Key_list = sorted(List)
    low = 0
    high = len(Key_list) - 1
    while low <= high:
        mid = (low + high)/2
        item = Key_list[mid]
        if LookedUp == item:
            return Key_list[mid]
        elif LookedUp < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def Menu():
    print "Type word you want to search"
    print "Type x to quit"
    global Entry
    Entry = raw_input("Please enter the word you want to search : ")
    if Entry == "x":
        abc567 = "Don't Continue" # Pointless line
    else:
        Process()
        
def Process():
    if S_Binary(Entry,Dict_keys()) == -1:
                Vrfctn = False
                for i in range(len(Dict_keys())):
                    if S_for_Alt(Entry,Dict_keys()[i]) == False:
                        abc123 = "Do nothing" #Pointless line
                    else:
                        Vrfctn = True
                        LookedUp = Dict_keys()[i] # Assign Alternative word to use later
                        break
                if Vrfctn == False:
                    LookedUp = Find_Cls(Entry,Dict_keys()) #Assign Closest word to use later
                Ask = raw_input("Did you mean : %s ?"%LookedUp)
                if Ask == "y":
                    print LookedUp," : ",dict1[LookedUp]
                    Menu()
                else:
                    Menu()
    else:
        LookedUp = S_Binary(Entry,Dict_keys())
        print LookedUp," : ",dict1[LookedUp]
        Menu()
    
        
dict1 = {}
for i in range(len(Dict_keys())):
    dict1[Dict_keys()[i]] = Dict_values()[i]
Menu()
