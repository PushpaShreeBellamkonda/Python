def sub_string(s1,s2):
    if s2 in s1:
        return s1.index(s2)
s1=input("enter a string: ")
s2=input("enter a substring: ")
print(sub_string(s1,s2))    
