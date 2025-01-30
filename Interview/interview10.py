# k = 12345

# iter = str(k)

# print(type(iter))

# list1 = []
# for i in iter:
#     list1.append(i)
# result = int("".join(map(str, list1)))
# print(result)

# another way of doing it but output in list

num_string="12345"
int_list=[int(char) for char in num_string]
print (int_list)

# another way 

# num_string="12345"
# num = int(num_string)
# print (type(num))
