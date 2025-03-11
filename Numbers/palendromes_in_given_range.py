def palendrome(num):
    rev=0
    num1=num
    while num>0:
        ld=num%10
        rev=(rev*10)+ld
        num=num//10
    return num1==rev

min=int(input("enter minimum number"))
max=int(input("enter maximum number"))

palindrome_list=[i for i in range(min,max+1) if palendrome(i)]
print(" palendromes list is",palindrome_list)