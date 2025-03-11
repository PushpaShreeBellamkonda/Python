def harshad_num(num):
    t_sum=sum(int(i) for i in str(num))
    return num % t_sum==0        
num=int(input("enter a number  :"))
print(harshad_num(num))