def gcd(d1,d2):
    while d2:
        d1,d2=d2,d1%d2
    return d1

def lcm(d1,d2):
    return (d1*d2)/gcd(d1,d2)

def add_frac(num1,num2,den1,den2):
    common_deno=lcm(den1,den2)
    print(common_deno)
    num1=num1*(common_deno//den1)
    num2=num2*(common_deno//den2)

    numerator=num1+num2
    denominator=common_deno

    # common_fac=gcd(numerator,denominator)
    # numerator//=common_fac
    # denominator//=common_fac

    return numerator,denominator
   
num1,den1=map(int,input("enter (n1,d1): ").split())
num2,den2=map(int,input("enter (n1,d2): ").split())

numerator, denominator=add_frac(num1,den1,num2,den2)
print(f"sum is : {numerator} / {denominator}")