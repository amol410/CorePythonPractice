# permutation and combination where i + j + k != n 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(new_list)  






l1 = [1,2,3,4]
l2 = [5,6,7,8]





