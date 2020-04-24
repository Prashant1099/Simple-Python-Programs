# This is a Python Program to take in the marks of 5 subjects and display the grade.

m1 = int(input("\nEnter marks of First Subject  = "))
m2 = int(input("Enter marks of Second Subject = "))
m3 = int(input("Enter marks of Third Subject  = "))
m4 = int(input("Enter marks of Fourth Subject = "))
m5 = int(input("Enter marks of Fifth Subject  = "))

per = (m1 + m2 + m3 + m4 + m5)/5

if per <= 60:
    grade = 'F'
elif per <= 70:
    grade = 'D'
elif per <= 80:
    grade = 'C'
elif per <= 90:
    grade = 'B'
else:
    grade = 'A'

print("-----------------")
print("Grade = ", grade)
print("-----------------")