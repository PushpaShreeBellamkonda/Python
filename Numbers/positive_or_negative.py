def positive_or_not(num):
    if num>0:
        return "Positive Number"
    elif num<0:
        return "Negative NUmber"
    else:
        return "Number is zero"

num=int(input("enter the number"))
print(positive_or_not(num))