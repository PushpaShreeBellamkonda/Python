def toh(n,a,b,c):
    if n==1:
        print(f"move 1 form  {a} to {c}")
    else:
        toh(n-1,a,c,b)
        print(f"move n from {a} to {c}")
        toh(n-1,b,a,c)

result=toh(3,'a','b','c')
print(result)