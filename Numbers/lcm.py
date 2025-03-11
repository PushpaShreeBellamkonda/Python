def lcm(n1,n2):
    gcd=1
    for i in range(1, min(n1,n2)+1):
        if (n1 % i==0 and n2 % i==0):
            gcd=i
    return (n1*n2)/gcd

n1=int(input("enter number1 : "))
n2=int(input("enter number2 : "))
print(lcm(n1,n2))