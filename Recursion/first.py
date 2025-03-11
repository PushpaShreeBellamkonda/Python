print("1st ONE")
# infinite run
# def fun1():
#     print("pushu")
#     fun1()
# fun1()
print("2nd ONE")
# # finite run

def fun2(n):
     if n==0:
        return
     print("pushu")
     fun2(n-1)
fun2(5)

# 321123 series
print("3rd ONE")

def fun2(n):
    if n==0:
        return
    print(n)
    fun2(n-1)
    print(n)
fun2(3)

# some other

print("4th ONE")

def fun2(n):
    if n==0:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)
fun2(3)

# some other


def fun(n):
    if n<=1:
        return 0
    else:
        return 1+fun(n//2)
fun(16)
