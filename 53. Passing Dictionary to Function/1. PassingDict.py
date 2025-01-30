# Passing Dictionary to Function
def show(d):
	print(d)
	print(type(d))
	for i in d:
		print(i,'=',d[i])

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}
show(dc)



