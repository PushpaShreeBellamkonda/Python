def isbalanced(exp):
    stack=[]
    for i in exp:
        if i in ('(','[','{'):
            stack.append(i)
        else:
            if not stack:
                return False
            elif mismatched(stack[-1],i)==False:
                
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
    
def mismatched(a,b):
    if (a=='(' and b==')') or (a=='[]' and b==']') or (a=='{' and b=='}'):
        return True
    else:
        return False
    
exp="{[()]}"
print(isbalanced(exp))




