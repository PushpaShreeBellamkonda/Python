arr=list(map(int,input("enter the values").split()))
print(arr)
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
print(min)