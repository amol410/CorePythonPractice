x = 1
y = 1
z = 2
n = 3

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                print([i,j,k])


new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

print(new_list)


# issue solved - issue was not able to make list[list] in 1st solution
# solved
result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                result.append([i,j,k])
                
print(result)