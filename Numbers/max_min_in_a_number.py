def max_min_in_a_number(num):
    maximum_num=max(int(i) for i in str(num))
    minimum_num=min(int(i) for i in str(num))
    return f" Largest Number is {maximum_num} \n Minimum Number is {minimum_num}"
num=int(input("enter a number: "))
print(max_min_in_a_number(num))