# The program takes both the values from the user and swaps them without using temporary variable.

a = int(input("\nEnter First Number  = "))
b = int(input("Enter Second Number = "))

a = a + b
b = a - b
a = a - b

print("----------------------")
print("After Swapping:")
print("----------------------")
print("First Number  = ", a)
print("Second Number = ", b)
print("----------------------")