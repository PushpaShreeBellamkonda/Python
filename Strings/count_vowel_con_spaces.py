def count_char(s):
    s1=list(s)
    vowel_count=0
    cons_count=0
    spaces_count=0
    for i in range(len(s1)):
        if (s1[i]=='a' or s1[i]=="e" or s1[i]=="i" or s1[i]=="o" or s1[i]=="u"):
            vowel_count+=1
        elif s1[i].isalpha() and s1[i] not in "aeiou":
            cons_count+=1
        else:
            spaces_count+=1

    print("No of Vowels are : ",vowel_count)
    print("No of Consonants are : ",cons_count)
    print("No of White spaces are : ",spaces_count)
    
s=input("enter the string: ")
count_char(s)