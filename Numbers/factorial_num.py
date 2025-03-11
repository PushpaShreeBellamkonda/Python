def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac*=i
    return fac
num=int(input("enter the number: "))
print(factorial(num))