# This is a Python Program to reverse a given number.

n = int(input("\nEnter any Number = "))

rev = 0
temp = n

while (n>0):
    mod = n % 10
    rev = rev*10 + mod
    n = n // 10

print("-----------------------------")
print("Reverse of ",temp," = ", rev)
print("-----------------------------")