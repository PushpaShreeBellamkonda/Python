from collections import Counter
def ispalendrome(s):
    cnt=Counter(s)
    odd=0

    for freq in cnt.values():
     
     if freq % 2 != 0:     #if freq % 2 != 0:: Inside the loop, this checks if freq (the count of a character) is odd. If it is, then freq % 2 will not equal 0, so this condition is True for characters with odd counts.    
            odd+=1
            if odd >1:
                return False
    return True

s="madam"
print(ispalendrome(s))


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