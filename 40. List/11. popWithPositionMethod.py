#pop(positon_number) method
a = [10, 20, 30, 10, 90, 'Geekyshows']

print("Before POP:", a)

n = a.pop(2)

print("After POP:", a)

# delete can delete entire list
# pop can remove last element easily
# delete can be used to delete half or customized string (slicing)

for element in a:
	print(element)
	
print("Removed Element:",n)