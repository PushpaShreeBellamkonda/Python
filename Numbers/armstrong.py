def armstrong_or_not(num):
    k=len(str(num))
    sum=0
    n=num
    while n>0:
        ld=n % 10
        sum+=ld**k
        n=n // 10
    return sum==num

num=int(input("enter the number"))
print(armstrong_or_not(num))