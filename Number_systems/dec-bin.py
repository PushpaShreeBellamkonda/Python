def dectobin(num):
    if num==0:
        return " "
    return dectobin(num//2) + str(num%2)

if __name__=='__main__':
    number=5
    res=dectobin(number)
    print(res)
