# Complete the solve function below.
def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s    

if __name__ == '__main__':
    s = input("Enter your first and last name: ")
    result = solve(s)
    print(result)

def solve(s):
    y = s.title()
    return y

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

# what does split does ? - 
# creates list from a string as below

x = "amol shinde"

y = x.split()

print(y)