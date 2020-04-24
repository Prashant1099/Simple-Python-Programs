# This is a Python Program to read a number n and print the natural numbers summation pattern.

r = int(input("\nEnter any Range = "))

print("-------------------------")
for row in range (1, r+1):
    a = []
    for col in range (1, row+1):
        a.append(col)
        if col == row:
            print(col, end=" = ")
        else:
            print(col, end=" + ")
    print(sum(a))
print("-------------------------")    