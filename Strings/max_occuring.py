from collections import Counter
def max_occuring(s):
    freq=Counter(s)
    print(freq)
    max_occur=max(freq,key=freq.get)
    return max_occur
s=input("enter a string: ")
print(max_occuring(s))