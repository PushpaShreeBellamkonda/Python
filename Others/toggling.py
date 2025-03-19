# convert a decimal number to binary and toggle its bits and print the value of toggled bits and if possible print the binary rep of toggled bits

def toggle_bits(n):
    binary=bin(n)[2:]
    print(binary)
    bits=len(binary)
    print(bits)
    bitmask=(1 << bits)-1
    print(bitmask)
    toggled_number=n^bitmask
    print(toggled_number)
    toggled_binary=bin(toggled_number)[2:].zfill(bits)   #zfill adds zeros on left side of string ,when the original string length is less than specified width   
    print(toggled_binary)

n=int(input("enter a number: "))
toggle_bits(n)