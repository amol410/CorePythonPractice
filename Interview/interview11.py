def swap_case(s):
    new_s = ""

    for i in range(len(s)):
        if s[i].islower():
            new_s += s[i].upper()
        else:
            new_s += s[i].lower()
    return new_s            

if __name__ == '__main__':
    s = "HackerRank"
    result = swap_case(s)
    print(result)


# def swapcase(string1):
#     swapped = string1.swapcase()
#     return swapped

# string1 = swapcase("HackerRank")

# print(string1)