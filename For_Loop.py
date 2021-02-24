#Prints 1 Mississippi etc up the the count of 5

for mississippi in range(1, 6): 
    print(mississippi, "Mississippi")

print("Ready or not, here I come!")


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break # stops the loop at 2 
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue #skips printing the loop for 3 and goes right to printing the loop for 4
    print("Inside the loop.", i)
print("Outside the loop.")
