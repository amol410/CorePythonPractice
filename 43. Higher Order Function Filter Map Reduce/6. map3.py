list1 = ["a","b","c","d"]
tuple1 = ("e","f","g","h")
list2 = ["9","6","5","8"]

x = "".join(list1)
y = "".join(tuple1)
z = "".join(map(str,list2))
zz = int("".join(map(str,list2)))

print(x)
print(y)
print(z)
print(type(z))
print(zz)
print(type(zz))