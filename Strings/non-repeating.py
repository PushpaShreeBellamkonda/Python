from collections import Counter
def non_repeating(s):
    freq=Counter(s)
    non_repeating=[]
    for i in freq:
        if freq[i]==1:
            non_repeating.append(i)
    return non_repeating

s=input("enter a string: ")
print(non_repeating(s))
