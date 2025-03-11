def remove_duplicates(s):
    seen=[]
    for i in s:
        if i not in seen:
            seen.append(i)
        s=s.replace(i,"")
    return "".join(seen)

s=input("enter a string: ")
print(remove_duplicates(s))