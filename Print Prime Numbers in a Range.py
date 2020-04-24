# This is a Python Program to print prime numbers in a range.

r = int(input("\nEnter any Range = "))

print("-----------------------------")
print("Prime Numbers upto range",r)
print("-----------------------------")
for i in range (1, r+1):
    count = 0
    n = i
    for j in range (1, n+1):
        if (n % j == 0):
            count += 1
        
    if count == 2:
        print(n)
print("-----------------------------")