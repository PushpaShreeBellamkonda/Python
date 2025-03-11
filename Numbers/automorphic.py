def automorphic_or_not(num):
    num1=num**2
    num2=num1 % 100
    if num2 == num:
        return "Its Automorphic Number"
    else:
        return "Its not Automorphic Number"
    
num=int(input("enter a number: "))
print(automorphic_or_not(num))

# n= 76 , its square should end with 76