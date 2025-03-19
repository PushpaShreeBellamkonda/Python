if __name__ == '__main__':
    s = input()
    is_alphanumeric=any(i.isalnum() for i in s)
    print(is_alphanumeric)
    is_alphabetic=any(i.isalpha() for i in s)
    print(is_alphabetic)
    is_digit=any(i.isdigit() for i in s)
    print(is_digit)
    is_lower=any(i.islower() for i in s)
    print(is_lower)
    is_upper=any(i.isupper() for i in s)
    print(is_upper)

