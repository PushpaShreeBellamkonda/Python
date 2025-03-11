def prime_or_not(num):
    count=0
    for i in range(1,num+1):
        if num % i ==0:
            count+=1
    return count==2
min=int(input("enter the start range: "))
max=int(input("enter the end range: "))
prime_list=[j for j in range(min,max+1) if prime_or_not(j)]
print("Prime Numbers in the above range are : " ,prime_list)


