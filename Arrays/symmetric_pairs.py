# arr=list(map(int,input("enter the values").split()))
# pairs=[]
# for i in range(len(arr)-1):
#     pairs.append((arr[i],arr[i+1]))
# print(pairs)
# seen=set()
# unseen=[]
# for i in range(len(pairs)):
#     if pairs[i] not in seen:
#         seen.add(pairs[i])
#     else:
#         unseen.append(pairs[i])
# print(unseen)

def symmetric_pairs(pairs):
    seen=set()
    result=[]
    for a,b in pairs:
        if (b,a) in seen:
            result.append((a,b))
        else:
            seen.add((b,a))
    return result

arr=list(map(int,input("enter the values").split()))
pairs=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        pairs.append((arr[i],arr[j]))
print(pairs)
print(symmetric_pairs(pairs))
    
