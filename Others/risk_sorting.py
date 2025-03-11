n=int(input("enter the range of array"))
arr=[]
risks=list(map(int,input("enter the risks").split()))
if len(risks)==n and all(0<=i<=2 for i in risks):
    for i in risks:
        arr.append(i)
else:
    print("enter risks from 0 to 2")
print(sorted(arr))
