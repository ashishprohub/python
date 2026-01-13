# Can we have a set with 18 (int) and '18' (str) as a value in it?

# set = {8, '8'}
# print(set)
# print(type(set))

my_set = {8, '8'}

for element in my_set:
    if isinstance(element, int):
        print(f"Value: {element} | Type: Integer (Numeric)")
    elif isinstance(element, str):
        print(f"Value: '{element}' | Type: String (Text)")