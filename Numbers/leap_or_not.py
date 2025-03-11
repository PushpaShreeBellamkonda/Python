def leap_or_not(year):
    if (year % 400 ==0 or (year % 4 ==0 and year %100 !=0)):
        return "leap Year"
    else:
        return "Non-Leap year"
    
year=int(input("enter the Year"))
print(leap_or_not(year))