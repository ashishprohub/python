# name = 'ashish'

# print(len(name)) 
# print(name.endswith('ish'))
# print(name.endswith('isha'))
# print(name.startswith('as'))
# print(name.startswith('aas'))

# statement = 'i am ashish'
# print(statement.capitalize())

# --------------------------------------------------
# 1. lower() / upper()
text = "Hello"
text.lower()   # 'hello'
text.upper()   # 'HELLO'

# ----------------------------------------------------
# 2. strip() / lstrip() / rstrip()
name = "  Ashish  "
name.strip()   # 'Ashish'

# -----------------------------------------------------
# split()
sentence = "I love Python"
sentence.split()   # ['I', 'love', 'Python']



# 4. join()
words = ['I', 'love', 'Python']
" ".join(words)   # 'I love Python'

# 5. replace()
text = "I like Java"
text.replace("Java", "Python")

# 6. find()/index()
text = "hello world"
text.find("world")   # 6

# 7. count()
text = "banana"
text.count("a")   # 3

# 8. startswith() / endswith()
file = "data.csv"
file.endswith(".csv")   # True

# 9. isalpha()/isdigit()/isalum()
"123".isdigit()    # True
"abc".isalpha()    # True

# 10. capitalize()/title()
name = "ashish kumar"
name.title()   # 'Ashish Kumar'

# 11. format()
name = "Ashish"
age = 20
f"My name is {name} and I am {age}"




