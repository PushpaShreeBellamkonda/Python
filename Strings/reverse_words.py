def reverse(s):
    words=s.split()
    return " ".join(words[::-1])

s=input("enter a string: ")
print(reverse(s))
