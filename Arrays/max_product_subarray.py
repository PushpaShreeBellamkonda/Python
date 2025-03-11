def symmetric_pairs(arr):
    pairs=[(arr[i],arr[i+1]) for i in range(len(arr)-1) ]
    seen=set()
    symmetric_pairs=[]
    for a,b in pairs:
        if (b,a) in seen:
            symmetric_pairs.append((b,a))
        else:
            seen.add((a,b))
    return symmetric_pairs

arr=list(map(int,input("enter the values").split()))
print(symmetric_pairs(arr))
