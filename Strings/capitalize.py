# capitalize the first and last letter in a word in a sentence
def capitalize(s):
    words=s.split()
    result=[]
    for i in words:
        if len(i)==1:
            result.append(i.upper())
        else:
            result.append(i[0].upper() + i[1:-1] + i[-1].upper())
    return " ".join(result)
s=input("enter a string: ")
print(capitalize(s))