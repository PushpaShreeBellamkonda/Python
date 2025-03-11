from collections import Counter
def sort_by_freq(arr):
    freq=Counter(arr)
    first_occ={val:idx for idx,val in enumerate(arr)}
    arr.sort(key=lambda x: (-freq[x],first_occ[x]))
    return arr
arr=list(map(int,input("enter the values").split()))
result=sort_by_freq(arr)
print(*result)