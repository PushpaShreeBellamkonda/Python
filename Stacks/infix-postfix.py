operators=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def in_pos(exp):
    stack=[]
    output=' '
    for i in exp:
        if i not in operators:
            output+=i
        elif i=='(':
            stack.append('(')
        elif i==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(i)

    while stack:
        output+=stack.pop()
    return output

exp=input("Give your infix expression:")
print("your postfix expression is",in_pos(exp))
