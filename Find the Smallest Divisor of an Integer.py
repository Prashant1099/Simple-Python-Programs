# This is a Python Program to find the smallest divisor of an integer.

n = int(input("\nEnter any Number = "))

print("-----------------------------")
for i in range (2, n+1):
    if (n % i == 0):
        print("Smallest divisor of",n, " = ",i)
        break
    print("-----------------------------")