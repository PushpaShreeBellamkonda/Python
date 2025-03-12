def dec_bin(n):
    if n==0:
        return ""
    return dec_bin(n // 2) + str(n % 2)
n=int(input("enter a number: "))
print(dec_bin(n))

