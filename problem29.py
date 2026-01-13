# Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter your first number:"))
a2 = int(input("Enter your first number:"))
a3 = int(input("Enter your first number:"))
a4 = int(input("Enter your first number:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Number a1 is greatest",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Number a2 is greatest",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Number a3 is greatest",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("Number a4 is greatest",a4)
