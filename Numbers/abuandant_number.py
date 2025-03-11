# sum of its factors is > the number
def abuandant(num):
    fac=[]
    for i in range(1,num):
        if num % i ==0:
            fac.append(i)
    sum_fac=0
    for i in range(len(fac)):
        sum_fac+=fac[i]
    return sum_fac > num

num=int(input("enter a number: "))
print(abuandant(num))