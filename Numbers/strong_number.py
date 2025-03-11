def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

def strong_num(num):
    temp=num
    sum_fac=0
    while temp > 0:
        ld=temp % 10
        sum_fac+=factorial(ld)
        temp = temp //10
    return sum_fac==num

num=int(input("enter a number :"))

if strong_num(num):
    print("Strong Number")
else:
    print("Not a Strong Number")