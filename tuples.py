# a = (1, 2, 3, 4, 5, 7, 6)
# print(type(a))

# -------------------------------
# making empty tuple 
# a = ()
# print(type(a))
# ------------------------
# Making tuple of single element
# a = (1)
# print(type(a))

# output is 
# <class 'int'>
        # So to make single element tuple we have to provide one comma after writing the element in the tuple 

# a =(1,)
# print(type(a))

# <class 'tuple'>

                                                # Tuple methods


a = (1, 45, 342, 3424, False, "Rohan", "Shivam")
# print(a)

no = a.count(45)
print(no)

i= a.index(3424)
print(i)
# -----------------------------------------------------------------
# Concatenation
tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenated = tuple1 + tuple2
print(concatenated)
# -----------------------------------------------------------------
# Repetition
my_tuple = (1,2,3,4,4)
repeated = my_tuple*3
print(repeated )
# -----------------------------------------------------------------
# Membership
my_tuple = (1,2,3,4)
print(4 in my_tuple)
print(5 in my_tuple)
# ---------------------------------------------------------------------------

my_tuple = (1,2,3,4)
print(len(my_tuple))

