octal=input("enter a octal number: ")
decimal=int(octal,8)
hexadecimal=hex(decimal)[2:].upper()
print(hexadecimal)