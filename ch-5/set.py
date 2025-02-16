s = set() # this is the way to create an empty set
print(type(s))
seeeeet = {} # iska type dict hoga jo ki empty hogi
print(type(seeeeet))

s1 = {1, 4, 6, 8}
s2 = {1, 3, 6, 79}


# methos in set
print(s1.union(s2))
print(s1.intersection(s2))

s1.add(57)
# s1.pop() # removes an arbitry element from the set
s1.remove(4) # gives an error when the element is not there
# print(len(s1))
s1.clear()
s1.add(4)
print(s1)

