s=input("enter a string")
count1=s.count('*')
count2=s.count('#')
print(count1)
print(count2)
if count1==count2:
    print(count1-count2,"both are equal")
elif count1 > count2:
    print(count1-count2,"no of * is greater than #")
else:
    print(count1-count2,"no of # is greater than *")

    