arr=list(map(int,input("enter the values").split()))
frequency={}
for i in arr:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for element,count in frequency.items():
    print(f"element {element} occurs {count} times")

