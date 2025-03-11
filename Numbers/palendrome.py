def palendrome(num):
    rev=0
    num1=num
    while num>0:
        ld=num%10
        rev=(rev*10)+ld
        num=num//10

    if num1==rev:
        return "palendrome Number"
    else:
        return "Not a palendrome Number"
print(palendrome(4554))
