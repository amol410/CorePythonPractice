# Check leap year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

xing = leap_year(2008)
print(xing)            

# if django-admin is not recognized
# python -m django startproject myproject

    