# If languages of two friends are same; what will happen to the program in problem 25? 
# Ans 
# Enter your friend's name:Ashish
# Enter your favorite language:HIndi
# Enter your friend's name:Rahul
# Enter your favorite language:HIndi
# Enter your friend's name:Ravi
# Enter your favorite language:Eng
# Enter your friend's name:Alok 
# Enter your favorite language:French
# {'Ashish': 'HIndi', 'Rahul': 'HIndi', 'Ravi': 'Eng', 'Alok ': 'French'}

# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

dic = {}

name = input("Enter your friend's name:")
lang = input("Enter your favorite language:")
dic.update({name: lang})

name = input("Enter your friend's name:")
lang = input("Enter your favorite language:")
dic.update({name: lang})

name = input("Enter your friend's name:")
lang = input("Enter your favorite language:")
dic.update({name: lang})

name = input("Enter your friend's name:")
lang = input("Enter your favorite language:")
dic.update({name: lang})

print(dic)

