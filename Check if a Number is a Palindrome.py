# This is a Python Program to check whether a given number is a palindrome.

n = int(input("\nEnter any Number = "))

rev = 0
temp = n

while (n>0):
    mod = n % 10
    rev = rev*10 + mod
    n = n // 10

print("-----------------------------")
if temp == rev:
    print(temp, " is a Palindrom Number")
else:
    print(temp, " is not a Palindrom Number")
print("-----------------------------")
