arr=list(map(int,input("enter the values").split()))
list=[]
for i in range(len(arr)):
    while arr[i] not in list:
        list.append(arr[i])
print(list)