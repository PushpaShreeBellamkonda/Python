n=int(input("enter the size of the array"))
arr=[]
items=list(map(int,input("enter items").split()))
if len(items)==n:
    for i in items:
        arr.append(i)
else:
    print("wrong output")

seen=set()
for i in range(len(arr)):
    while arr[i] in seen:
        arr[i]+=1
    seen.add(arr[i])
final_arr=print(arr)

count=0
for i in range(len(arr)):
    count+=arr[i]
print(count)
    
