def remove_brackets(exp):
    brackets={'(',')'}
    exp1=(i for i in exp if i not in brackets)
    return "".join(exp1)

exp=input("enter a expression: ")
print(remove_brackets(exp))