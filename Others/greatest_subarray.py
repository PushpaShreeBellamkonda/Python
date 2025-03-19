def subarrays(arr,size):
    subs=[arr[i:i+size] for i in range(0,len(arr),size)]
    max_sub=max(subs,key=lambda x:x.count('a'))
    return max_sub.count('a')
arr=['a','a','a','b','a','a','b']
size=3
print(subarrays(arr,size))