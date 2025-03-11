import math
def quad_roots(a,b,c):
    d=(b**2)-4*a*c

    if d>0:
        root1=(-b + math.sqrt(d))/(2*a)
        root2=(-b - math.sqrt(d))/(2*a)
        print(f" Real and Distinct roots : {root1} , {root2}")
    elif d==0:
        root=-b/(2*a)
        print(f"Real and Equal roots: {root}")
    else:
        real_part=-b/(2*a)
        imaginary_part=math.sqrt(abs(d))/(2*a)
        print(f"Complex roots: {real_part} , {imaginary_part}")

a,b,c=map(float,input("enter co-effecients a,b,c: ").split())
quad_roots(a,b,c)