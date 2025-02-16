s = set()
s.add(20)
s.add(20.00)
s.add("20")

print(len(s)) # length of s comes out to be 2 but it should be 3?
# it is because python treats 1 and 1.00 equally (1 = 1.00) but 1 != 1.10