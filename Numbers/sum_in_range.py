def sum_in_range(l,r):
    sum=0
    for i in range(l,r+1):
        sum+=i
    return sum
l=int(input("enter a number: "))
r=int(input("entera number: "))
print(sum_in_range(l,r))