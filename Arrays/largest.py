arr=list(map(int,input("enter the values").split()))
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max)