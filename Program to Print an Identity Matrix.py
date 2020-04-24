# This is a Python Program to read a number n and print an identity matrix of the desired size.

r = int(input("\nEnter any Range = "))

print("-------------------")
for row in range (1, r+1):
    for col in range (1, r+1):
        if row == col:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
print("-------------------")