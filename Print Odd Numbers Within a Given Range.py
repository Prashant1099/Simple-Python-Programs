# This is a Python Program to print odd numbers within a given range.

r = int(input("\nEnter Range = "))

sum = 0
for i in range (1, r+1, 2):
    sum += i

print("-------------------------------------------------------")
print("Summation of Odd numbers within range",r, " = ",sum)
print("-------------------------------------------------------")