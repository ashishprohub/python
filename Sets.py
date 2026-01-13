# s = set()           # no repetition allowed
# s.add(1)
# s.add(2)            # or set = (1,2)
# print(s)

# -------------------------------------------------------

# Operations on sets 
# `s = {1,2,3,4,8}` is creating a set named `s` with elements 1, 2, 3, 4, and 8. Sets in Python are
# unordered collections of unique elements, so any duplicate elements will be automatically removed.
# s = {1,2,3,4,8}

# print(len(s))               # 5

# s.remove(3)
# print(s)                    #{1, 2, 4, 8}

# s.pop()
# print(s)                       #{2, 3, 4, 8} Remove any random element from set

# s.clear()
# print(s)                     # set()

# s = s.union({1,8,10,11})
# print(s)                        #{1, 2, 3, 4, 8, 10, 11}

# s = s.intersection({2,3,5,6})
# print(s)                        #{2, 3}


# s1 = {1,2,35,65,36,67,48}
# s2 = {48,58,29,50,67,35,65}

# print(s1.union(s2))                     #{65, 1, 2, 35, 36, 67, 48, 50, 58, 29}
# print(s1.intersection(s2))              #{48, 65, 67, 35}



