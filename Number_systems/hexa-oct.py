hexanumber=input("enter a number: ")
decimal=int(hexanumber,16)
octal=oct(decimal)[2:]
print(octal)