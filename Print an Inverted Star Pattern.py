# This is a Python Program to read a number n and print an inverted star pattern of the desired size.

r = int(input("\nEnter any Range = "))

print("--------------------")
for row in range (1, r+1):
    for sp in range (1, row):
        print("  ", end="")
    for col in range (1, r-row+2):
        print(" *", end="")
    print()
print("--------------------")
