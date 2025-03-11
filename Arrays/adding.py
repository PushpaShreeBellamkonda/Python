def insert_beg(arr,x):
    arr.insert(0,x)
    return arr
    
def insert_end(arr,x):
    arr.append(x)
    return arr

def insert_pos(arr,pos,x):
    arr.insert(pos,x)
    return arr

arr=list(map(int,input("enter the values").split()))
print(insert_beg(arr,10))
print(insert_end(arr,20))
print(insert_pos(arr,3,40))