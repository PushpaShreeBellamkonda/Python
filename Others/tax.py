n=int(input("enter a number"))
arr=[int(input()) for _ in range(n)]
odds=[]
for i in range(n):
    if arr[i]%2!=0:
        odds.append(arr[i])
print(odds)
count=len(odds)
tax=int(input("enter tax"))
date=int(input("enter date"))
d=date%10
if d%2==0:
    total_tax=count*tax
print(total_tax)