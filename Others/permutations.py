n=int(input("enter n:"))
m=int(input("enter m:"))
o=int(input("enter o:"))
s=int(input("enter s:"))
p=[[i,j,k] for i in range(n+1) for j in range(m+1) for k in range(o+1) if i+j+k!=s]
print(p)