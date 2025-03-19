n=int(input("enter a range: "))
students={}
for i in range(n):
    name=input("enter the name: ")
    grade=float(input("enter the grade: "))
    students[name]=grade
sorted_dict=dict(sorted(students.items(),key=lambda item:item[1]))
min_key=min(students,key=students.get)
min_val=students[min_key]
print(min_val)