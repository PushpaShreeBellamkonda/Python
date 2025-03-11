# def bin_dec(n):
#     decimal=0
#     i=0
#     while(n!=0):
#         ld=n%10
#         decimal=decimal+ld* pow(2,i)
#         n=n//10
#         i+=1
#     return decimal

# n=int(input("enter the binary value: "))
# print(bin_dec(n))

binary=input("enter a number:")
decimal=int(binary,2)
print(decimal)