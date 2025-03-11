def remove_spec_char(s):
    s1=''.join(i for i in s if i.isalpha())
    print(s1)
s=input("enter a string :")
remove_spec_char(s)