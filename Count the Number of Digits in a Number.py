# The program takes the number and prints the number of digits in the number.

n = int(input("\nEnter any Number = "))

count = 0
temp = n
while (n>0):
    n //= 10
    count += 1

print("-----------------------------------")
print("Number of Digits in ",temp, " = ",count)
print("-----------------------------------")