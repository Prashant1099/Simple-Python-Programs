# This is a Python Program to read a number n and compute n+nn+nnn.

n = int(input("\nEnter any Number = "))

temp = str(n)

nn = temp + temp
nnn = nn + temp

sum = n + int(nn) + int(nnn)

print("--------------------------------")
print("Sum of n+nn+nnn = ", sum)
print("--------------------------------")