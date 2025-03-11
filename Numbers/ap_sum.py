def ap_sum(a,d,n):
    return ((n/2)*(2*a+(n-1)*d))
    # sum=0
    # i=0
    # while i < n:
    #     sum+=a
    #     a+=d
    #     i+=1
    # return sum
n=int(input("enter the no of items"))
a=int(input("enter the first term"))
d=int(input("enter the common difference"))
print(ap_sum(a,d,n))