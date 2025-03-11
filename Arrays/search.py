def search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
arr=list(map(int,input("enter the values").split()))
k=int(input("enter the element"))
print(search(arr,k))