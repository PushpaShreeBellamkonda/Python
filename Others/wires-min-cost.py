def min_cost(arr):
    if len(arr)<2:
        return None
    min_pair=(arr[0],arr[1])
    for i in range(0,len(arr)-1):
        if (arr[i],arr[i+1]) < (min_pair):
            min_pair=(arr[i],arr[i+1])
    pair=list(min_pair)
    print(pair)
    count=0
    for i in pair:
        count+=i
    arr.remove(min_pair)
    print(arr)

arr=list(map(int,input("enter the items ofarray: ").split()))
print(min_cost(arr))