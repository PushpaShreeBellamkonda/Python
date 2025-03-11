dict={1:"hii",2:"hello",3:"welcome"}
print(dict)
dict[4]="namaste"
print(dict[4])
print(dict.get(1))
print(dict.get(5))
print(dict.get(5,"Na"))
if 6 in dict:
    print(dict[6])
else:
    print("NA")

dict[2]="heee"
print(dict)
print(len(dict))
x=dict.pop(2)
print(x)
print(dict)
del dict[3]
print(dict)
print(dict.popitem())