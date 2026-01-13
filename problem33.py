# Write a program which finds out whether a given name is present in a list or not. 
list = [1, 2, 3, 4, "Ashish", False, True]
name = input("Enter your value to find in the list: ")
if (name in list):
    print("Your value is found in list successfully.....")
else:
    print("Your given value not found in the list")