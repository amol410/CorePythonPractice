# def print_numbers(n=1):
#     if n > 100:
#         return
#     print(n)
#     print_numbers(n + 1)
# print_numbers()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
fact_no = factorial(5)

print(fact_no)




