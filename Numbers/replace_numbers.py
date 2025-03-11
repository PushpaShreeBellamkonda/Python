def replace_num(num):
    num1=list(str(num))
    for i in range(len(num1)):
        if num1[i]=='0':
            num1[i]='1'
    return int("".join(num1))
num=int(input("enter a number: "))
print(replace_num(num))