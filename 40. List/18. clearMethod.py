#clear() Method
a = [10, 5, 90, 10, 30]

print("Before Clear",a)

a.clear()

print("After Clear",a)



xyz = [5,5,3,3,9,4,3,5,8,4,4,1]

unique =[]
for num in xyz:
    if xyz.count(num) == 1:
        unique.append(num)
print(unique)        