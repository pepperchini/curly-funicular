income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = float((income * .18) - 556.02)
    if tax <= 0: #nested if to get the tax to zero if it's a negative amount
        tax = 0.0

elif income > 85528:
    tax = 14839.02 + ((income - 85528) * .32)



tax = round(tax, 0)
print("The tax is:", tax, "thalers")
