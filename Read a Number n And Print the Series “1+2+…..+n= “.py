# This is a Python Program to read a number n and print and compute the series “1+2+…+n=”.

r = int(input("\nEnter any Range = "))

a = []
print("------------------------")
for i in range (1, r+1):
    a.append(i)
    if i != r:
        print(i, end="+")
    else:
        print(i, end=" = ")
print(sum(a))
print("------------------------")

# sum = 0
# for i in range (1, r+1):
#     sum += i

# print("-----------------------------")
# for i in range (1, r+1):
#     if i != r:
#         print(i, end="+")
#     else:
#         print(i, end=" = ")
# print(sum)
# print("-----------------------------")