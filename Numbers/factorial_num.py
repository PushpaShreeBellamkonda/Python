# def factorial(num):
#     fac=1
#     for i in range(1,num+1):
#         fac*=i
#     return fac
# num=int(input("enter the number: "))
# print(factorial(num))

def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
n=int(input("enter the number: "))
print(factorial(n-1)*2)