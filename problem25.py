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

