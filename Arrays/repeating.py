arr=list(map(int,input("enter the values").split()))
list=[]
repeats=[]
for i in range(len(arr)):
    if arr[i] not in list:
        list.append(arr[i])
    else:
        repeats.append(arr[i])
print(list)
print(repeats)
