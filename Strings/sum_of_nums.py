def sum_of_num(s):
    sum=0
    numbers=[int(i) for i in s if i.isdigit()]
    for i in numbers:
        sum+=i
    return sum

s=input("enter a string with digits :")
print(sum_of_num(s))

    