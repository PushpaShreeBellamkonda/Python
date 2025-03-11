def equilibrium_index(arr):
    left_sum=0
    total_sum=sum(arr)
    for i ,j in enumerate(arr):
        total_sum-=j
        if left_sum==total_sum:
            return i
        left_sum+=j
    return -1
arr=list(map(int,input("enter the values").split()))
print(equilibrium_index(arr))