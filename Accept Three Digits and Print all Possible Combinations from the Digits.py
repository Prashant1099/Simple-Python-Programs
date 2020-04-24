# This is a Python Program to accept three distinct digits and print all possible combinations from the digits.

a = int(input("\nEnter First Number  = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number  = "))

List = []

List.append(a)
List.append(b)
List.append(c)

for i in range (3):
    for j in range (3):
        for k in range (3):
            if (i!=j & j!=k & k!=i):
                print(List[i],List[j],List[k])