# This is a Python Program to find the sum of digits in a number.

n = int(input("\nEnter any Number = "))

sum = 0
temp = n
while (n>0):
    mod = n % 10
    sum += mod
    n = n // 10

print("-----------------------------------------")
print("Summation of digits in", temp, " = ", sum)
print("-----------------------------------------")