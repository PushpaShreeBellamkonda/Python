def count_substring(string, sub_string):
    return string.count(sub_string)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



# for all test cases
def count_substring(string, sub_string):
    i=0
    if string.find(sub_string)!=-1:
        i+=1
        while True:
            string=string[string.find(sub_string)+1:]
            if string.find(sub_string)!=-1:
                i+=1
            else:
                break
    return i

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)