from collections import Counter
def duplicates(s):
    freq=Counter(s)
    max_occur=max(freq,key=freq.get)
    s=s.replace(max_occur,"")
    return s
s=input("enter a string: ")
print(duplicates(s))
# removing most occuring character