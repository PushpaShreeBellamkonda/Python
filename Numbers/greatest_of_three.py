def greatest_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
num3=int(input("enter number3: "))
print(greatest_of_three(num1,num2,num3))