def even_or_odd(num):
    if num % 2==0:
        return "even"
    else:
        return "odd"
num=int(input("enter a number"))
print(even_or_odd(num))