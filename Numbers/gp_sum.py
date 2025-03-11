def gp_sum(n,a,r):
    sum=0
    i=0
    while i < n:
        sum=sum+a
        a*=r
        i+=1
    return sum

a=float(input("enter the first term"))
r=float(input("enter the common difference"))
n=int(input("enter the no of items"))
print("%5f" %gp_sum(a,r,n))