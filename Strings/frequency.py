from collections import Counter
def frequency(s):
    freq=Counter(s)
    return freq
s=input("enter a string: ")
print(frequency(s))
