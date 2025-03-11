def sum_of_N_Natural(n):
    for i in range(1,n):
        sum=n*(n+1)//2
    return sum
n=int(input("enter the number"))
print(sum_of_N_Natural(n))
    