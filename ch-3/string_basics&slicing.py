#  can be defined using 3 types
a = "harsh"
b = 'harsh'
c = '''harsh'''

# print(a,"\n",b, c)

print(a[1:4])  # a[start_index : last_index(which will not be printed)]
print(b[:])
print(c[1:])

d = "abcdefghijklmnopqrstuvwxyz"
print(d[0 : 27 : 2]) # [start_index : last_index : jump_step]