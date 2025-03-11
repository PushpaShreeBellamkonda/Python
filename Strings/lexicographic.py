def lexico(s):
    result=[]
    for i in s:
        if i.isalpha():
            if i=='z':
                result.append('a')
            elif i=='Z':
                result.append('A')
            else:
                result.append(chr(ord(i)+1))
        else:
            result.append(i)
    return "".join(result)
s=input("enter a string : ")
print(lexico(s))
