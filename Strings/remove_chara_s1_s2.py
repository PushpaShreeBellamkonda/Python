def remove_char(s1,s2):
    for i in s2:
        s1=s1.replace(i,"")
    return s1

s1=input("enter string1: ")
s2=input("enter string2: ")
print(remove_char(s1,s2))