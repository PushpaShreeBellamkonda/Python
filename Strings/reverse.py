def reverse(s):
    s1=list(s)
    return ''.join(s1[::-1])
s=input("enter a string: ")
print(reverse(s))