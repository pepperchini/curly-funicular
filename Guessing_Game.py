secret_number = 16

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter a number: "))

while number != secret_number:
    if number < secret_number:
        print("You're stuck in my loop! To get out you must guess a bigger number.")
    elif number > secret_number:
        print("You're stuck in my loop! To get out you must guess a lower number.")
    number = int(input("Try again!: "))
        
else:
    print("Well done, muggle! You are free now!")
    
