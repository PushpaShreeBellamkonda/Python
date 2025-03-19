# right triangle
n=5
for i in range(1,n+1):
    print("*"*i)

print()

# left triangle
n=5
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i)

print()

# inverted right
n=5
for i in range(n,0,-1):
    print("*"*i)

print()

# inverted left
n=5
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*i)