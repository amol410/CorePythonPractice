def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print_full_name(first_name, last_name)