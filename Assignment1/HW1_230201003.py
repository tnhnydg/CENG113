#Student ID : 230201003
A = input("Please enter your age:") #Asking for age
G1 = raw_input("Please enter your gender:") #Asking for gender (Used raw_input because Gender should be taken as string)
H = input("Please enter your height in centimetre:") #Asking for height in centimetre
W = input("Please enter your weight in kilogram:") #Asking for weight in kilogram
G = G1.lower() #For case insensitive
if A < 30 :
    if G == "man":
        n = 5.0
        m = 5.0
        c = 10.0*W + 6.25*H - n*A + m #Calorie per day
        print c #Shows calorie per day value
    elif G == "woman":
        n = 5.0
        m = -161.0
        c = 10.0*W + 6.25*H - n*A + m #Calorie per day
        print c #Shows calorie per day value
else :
    if G == "man":
        n = 7.0
        m = 5.0
        c = 10.0*W + 6.25*H - n*A + m #Calorie per day
        print c #Shows calorie per day value
    elif G == "woman":
        n = 7.0
        m = -161.0
        c = 10.0*W + 6.25*H - n*A + m #Calorie per day
        print c #Shows calorie per day value
