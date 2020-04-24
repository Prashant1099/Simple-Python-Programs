# The program takes the elements of the list one by one and displays the average of the elements 
# of the list.

r = int(input("\nEnter the Range = "))
print("--------------------")
l = []

for i in range (1, r+1):    
    n = int(input("Enter Number = "))
    l.append(n)

avg = sum(l)/r

print("--------------------")
print("Average = ", avg)
print("--------------------")