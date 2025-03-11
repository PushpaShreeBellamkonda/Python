# reverse a string
string="pushpa"
rev=" "
for i in string:
    rev=i + rev
print(rev)

# ord 

print(ord('a'))
print(ord('A'))
print(chr(77))
print(chr(88))

s="pushpa"
print(s[0])
print(s[1])

# use quotes
s1="""
hii
how 
are 
you
  """

print(s1)


# three ways to write  a string
# 1
name="pushpa"
place="Hyd"
s="hello %s welcome to %s"%(name,place)
print(s)

# 2

name="pushpa"
place="Hyd"
s1="hello {0} welcome to {1}".format(name,place)
print(s1)
# 3

name="pushpa"
PLACE="Hyd"
s2=f"hello {name} welcome to {place}"
print(s2)


# upper and lower

name="pushpa"
place="Hyd"
s2=f"hello {name.upper()} welcome to {PLACE.lower()}"
print(s2)

# finding substrings

s1="geeksforgeeks"
s2="geeks"
print(s2 in s1)

# r index , length , startswith , endswith

s1="geeksforgeeks"
s2="geeks"

print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2,0,13))
print(len(s1))
print(s1.startswith("geeks"))
print(s1.endswith("geeks"))
print(s1.startswith("geeks",1))
print(s1.endswith("geeks",8,len(s1)))


# split , join 

s1="geeks for geeks"
print(s1.split())
s2="geeks , for , geeks "
print(s2.split(","))

l=["pushpa" , "nithin" , "amar"]
print(" ".join(l))
print(" ,".join(l))


# lstrip , rstrip

l1="-----hiiii-----"
print(l1.strip("-"))
print(l1.rstrip("-"))
print(l1.lstrip("-"))

# find , -1 indicates not found

print(s1.find("geeks"))
print(s1.find("gfg"))
n=len(s1)
print(s1.find(s2,1,n))

# pattern searching in python
txt=input("enter pattern")
pat=input("enter pattern")
pos=txt.find(pat)
while pos >=0:
    print(pos)
    pos=txt.find(pat,pos+1)


# palendrome

string=input("enter your string")
low=0
high=len(string)-1
while low < high:
    if string[low] != string[high]:
        print("no")
        break
    low+=1
    high-=1
else:
    print("YES")


# Anagram naive solution

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    if(s1==s2):
        return True
    return False
s1="pushpa"
s2="ppusha"
s=anagram(s1,s2)
print(s)
    
# Anagram normal solution
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count=[0]*256
    for i in range (len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for i in count:
        if i !=0:
            return False
    return True
s1="pushpa"
s2="ppusha"
s=anagram(s1,s2)
print(s)























