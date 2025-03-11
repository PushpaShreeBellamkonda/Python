def largest_word(s):
    words=s.split()
    return max(words,key=len)

s=input("enter a string")
print(largest_word(s))