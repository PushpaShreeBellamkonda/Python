def sub_arrays(arr,arr1):
    subsets=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            subsets.append(arr[i:j+1])
    for i in range(len(subsets)):
        if arr1 in subsets:
            return True
        else:
            return False

arr=list(map(int,input("enter the values: ").split()))
arr1=list(map(int,input("enter the values: ").split()))
print(sub_arrays(arr,arr1))