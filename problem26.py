# If the names of 2 friends are same; what will happen to the program in problem 25? 

# The most latest value will be shown against key in the dictionary 

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

#Output:

# Enter your friend's name:Ashish
# Enter your favorite language:Hindi
# Enter your friend's name:Ashish
# Enter your favorite language:German
# Enter your friend's name:Alok
# Enter your favorite language:French
# Enter your friend's name:Alok
# Enter your favorite language:Bengali
# {'Ashish': 'German', 'Alok': 'Bengali'}


