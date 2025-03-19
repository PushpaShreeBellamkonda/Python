# from a given array if array contains zeros , push them to the end of the array

def zero_end(arr):
    non_zeros=[i for i in arr if i!=0]
    zero_count=arr.count(0)
    arr[:]=non_zeros + [0]*zero_count
    return arr

arr=list(map(int,input("enter array items: ").split()))
print(zero_end(arr))


            


