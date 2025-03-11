def reverse_number(num):
    rev=0
    num1=num
    while num1 >0:
        ld=num1%10
        rev=(rev*10)+ld
        num1=num1//10
    return rev
num=int(input("enter a number: "))
print(reverse_number(num))