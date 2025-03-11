# n=list(map(int,input("enter a number").split(',')))
# count=[]
# for i in range(len(n)-1):
#     count.append(n[i]*n[i+1])
# print(count)


n=input()
product=1
for digit in n:
    product=product*(int(digit))
print(product)
