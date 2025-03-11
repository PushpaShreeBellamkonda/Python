def fun(n):
    if n<=1:
        return 0
    else:
        return 1+fun(n//2)
print(fun(16))

# binary representation of a number
def fun1(n):
    if n==0:
        return
    fun1(n//2)
    print(n%2)
print(fun1(5))

# print numbers  from n to 1 
def funx(n):
    if n==0:
        return
    print(n)
    funx((n-1))
funx(5)

# print numbers  from 1 to n

def funx(n):
    if n==0:
        return
    funx((n-1))
    print(n)
funx(5)

# print sum of digits


def funx(n):
    if n<10:
        return n
    return funx(n//10)+n%10

print("the sum is :",funx(666))