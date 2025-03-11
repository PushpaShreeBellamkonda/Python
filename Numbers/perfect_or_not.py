def perfect_or_not(num):
    if num<2:
        return False
    sum_factors=(i for i in range(1,num) if num%i==0)
    return sum_factors

num=int(input("enter the number"))
if perfect_or_not(num):
    print("Perfect Number")
else:
    print("NOt Perfect Number")
