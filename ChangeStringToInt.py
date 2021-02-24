x = "1"

if x == 1: #This is false because "1" is a string not an int so we move to the next line
    print("one")
elif x == "1": #This is true because it is a string just like the original x value
    if int(x) > 1: #Does not execute because x is not > 1
        print("two")
    elif int(x) < 1: #Does not execute because x is not < 1
        print("three")
    else:
        print("four") #Executes because x == "1"
if int(x) == 1: #This line changes x to an int making the program print "five" because the statement is now True (x == int 1)
    print("five")
else: #Does not execute because the "if" statement above it is True. else only executes if the "if" statement above is False. Each "else" is tied to the previous "if".
    print("six")