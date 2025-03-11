def factors(num):
    fac_count=[]
    for i in range(1,num+1):
        if num % i ==0:
            fac_count.append(i)
    return fac_count

num=int(input("enter the number: "))
print(factors(num))