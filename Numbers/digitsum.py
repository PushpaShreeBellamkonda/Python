n=input("enter a number")
r=input("enter r value")
if not n.isdigit() or not r.isdigit():
    print("please enter a valid number")
    exit()

sum_num=sum(map(int,n))
print(sum_num)
r_sum=sum_num*int(r)
print(r_sum)
final_sum=sum(map(int,str(r_sum)))
print(final_sum)
