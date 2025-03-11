def dectoocta(num):
    if num==0:
        return " "
    return dectoocta(num//8) + str(num%8)

if __name__=='__main__':
    number=45
    res=dectoocta(number)
    print(res)
