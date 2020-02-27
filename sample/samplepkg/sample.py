print("sample text")
a = [1, 2, 3, 4, 5]

# Colon usage in list
print(a[5:])
print(a[2:])
print(a[:2])
print(a[:1])
print((a[:-2]))
print(a[-3:])

# Object on fly and checking the existence of value in any of the items in a list
w = type('', (), {})()
w.name = 'win'
x = type('', (), {})()
x.name = 'loss'
y = type('', (), {})()
y.name = 'no'
z = type('', (), {})()
z.name = 'way'

b = [w, x, y, z]
print(any(val.name == "win" for val in b))

# checking the existence in a dictionary
dic = {'a': 1,
       'b': 2,
       'c': 3}

print(('c' in dic))
