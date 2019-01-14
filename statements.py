#Declare variables
Day = "Sunday"
#Converting strings to integer
Hours = int("12")
Msg = "Good Morning"
#creating function
def Greetings():
    #checking for 2 match parameters
    if Hours == 12 and Day == "Monday":
        print(True)
    elif Hours == 12 and Msg == "Good Morning":
        print(True)
    elif Day == "Monday" and Msg == "Good Morning":
        print(True)
    else:
        print(False)

#output function
Greetings()
#output = True as it matches 2nd condition