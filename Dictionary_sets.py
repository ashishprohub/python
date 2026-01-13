# dic = {
#     "Ashish" : 10,
#     "Ravi" : 20
# }
# print(dic["Ashish"])
# print(dic.items())
# print(dic.keys())
# print(dic.values())
# --------------------------------------------------------------------
# Methods in dictionary
a = {
    "name" : "Ashish",
    "Age" : 20,
    "Marks" : [90,98,99]
}
# print(a.items())  
# Output [# dict_items([('name', 'Ashish'), ('Age', 20), ('Marks', [90, 98, 99])])]

# print(a.keys())
#Output [dict_keys(['name', 'Age', 'Marks'])]

# print(a.values())
#Output [dict_values(['Ashish', 20, [90, 98, 99]])]

# a.update({"name": "Mr. Ashish", "Designation" : "CEO"})
# print(a)
# Output
#{'name': 'Mr. Ashish', 'Age': 20, 'Marks': [90, 98, 99], 'Designation': 'CEO'} 

# print(a.get("name"))          # Output: Ashish
# print(a.get("Ashish2"))       # Output: None
# print(a["Harry2"])              # Error



