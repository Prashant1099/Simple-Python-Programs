# This is a Python Program to print all numbers in a range divisible by a given number.

lr = int(input("\nEnter Lower Range = "))
ur = int(input("Enter Upper Range = "))
n = int(input("\nEnter Number to be divided with = "))

for i in range (lr, ur+1):
    if (i % n == 0):
        print(i)
