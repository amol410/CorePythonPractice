a = [10, 20, -50, 21.3, 'Geekyshows']
print(a, id(a))
print(a[1])
a[1] = 40
print(a[1])
print(a, id(a))

# insert vs modify --> 
# insert - element wont be deleted
# modify via indexing - element will be replaced
# if we modify list through indexing its id wont be changed


import copy

Original = ['grapes',['apple', 'mango']]

deepcopy = copy.deepcopy(Original)

deepcopy[1][0] = "pineapple"

print(Original)
print(deepcopy) 
print(id(Original))
print(id(deepcopy))


shallow_copy = copy.copy(Original)

shallow_copy[1][0] = "pineapple"

print(Original)
print(shallow_copy)

print(id(Original))
print(id(shallow_copy))


