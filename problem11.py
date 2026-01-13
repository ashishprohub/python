# Write a program to fill in a letter template given below with name and date 
letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''
# name = input("Enter your name:")
# date = input("Enter latter's date")
# print(f"Dear {name},\n Yor are selected! \n {date}")
name = input("Enter name:")
date = input("Enter date: ")
print(letter.replace("<|Name|>",name) .replace("<|Date|>", date))