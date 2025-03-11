def remove_vowels(s):
    vowels={'a','e','i','o','u'}
    s1=[i for i in s if i.lower() not in vowels]
    return "".join(s1)

s=input("enter a string :")
print(remove_vowels(s))