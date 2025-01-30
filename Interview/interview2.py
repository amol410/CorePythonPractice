# def issubsequence(string, substring):
#     i = 0 
#     j = 0
#     while i < len(substring) and j < len(string):
#         if substring[i] == string[j]:
#             i += 1
#         j += 1 
#     return i == len(substring)   

# string = "abcdefghij"
# substring = "adi"
# result = issubsequence(string, substring)
# print(result)


def issubsequence(string, substring):
    i = 0 
    j = 0

    while i < len(substring) and j < len(string):
        if substring[i] == string[j]:
            i += 1
        j += 1
    return i == len(substring)
        
string = "abcdefghij"
substring = "adi"
result = issubsequence(string, substring)
print(result)