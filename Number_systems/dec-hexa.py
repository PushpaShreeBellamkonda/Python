def dectohexa(num):
    if num==0:
        return " "
    return dectohexa(num//16) + str(num%16)

if __name__=='__main__':
    number=69
    res=dectohexa(number)
    print(res)
