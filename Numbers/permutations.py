# permutations in which N people can occupy R seats
def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial

def permutations(n,r):
    return (factorial(n)/factorial(n-r))

n=int(input("enter n value:: "))
r=int(input("enter r value: "))
print(permutations(n,r))
