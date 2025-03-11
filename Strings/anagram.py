from collections import Counter
def anagram(s1,s2):
    return Counter(s1)==Counter(s2)
s1=input("enter string1: ")
s2=input("enter string2: ")
print(anagram(s1,s2))