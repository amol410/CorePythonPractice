#Variable Length Arguments
#Example 1
def add(x, y):
	z = x+y
	print("Addition:", z)
	
add(5, 2)

#Example 2
def add(*num):
	
	z = num[0]+num[1]+num[2]
	print("Addition:", z, num[3])
	
add(5, 2, 4, "zing")

#Example 3 # POSITIONAL ARGUMENT FIRST THEN VARIABLE LENGTH ARGUMENT
def add(x, *num):
	z = x+num[0]+num[1]
	print("Addition:", z)
	
add(5, 2, 4)
