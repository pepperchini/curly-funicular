#Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter
#and prints the string with enough leading spaces so that the last letter of the string is in column 70
#of the display.

def right_justify(s):
    #create variable 'a' then create an empty space
    #multiply the empty space by 70 minus the length of s then add in s
    a = " " * (70 - len(s)) + s 
    #finally print a
    print(a)
right_justify('montypython')