def prime_or_not(num):
    count=0
    for i in range(1,num+1):
        if num % i==0:
            count+=1
    if count==2:
        return "Prime Number"
    else:
        return "Not a prime NUmber"
    
num=int(input("enter a number"))
print(prime_or_not(num))