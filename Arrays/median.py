def find_median(arr):   
    n=len(arr)
    mid=n//2
    sorted_arr=sorted(arr)

    if n % 2 ==0:
        return (arr[mid-1]+arr[mid])/2
    else:
        return arr[mid]
    
arr=list(map(int,input("enter the values").split()))
print(find_median(arr))
