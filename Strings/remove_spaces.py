def remove_spaces(s):
    spaces={" "}
    s1=[i for i in s if i.lower() not in spaces]
    return "".join(s1)

s=input("enter a string :")
print(remove_spaces(s))