if __name__ == '__main__':
    n = int(input())
    integer_list =tuple(map(int, input().split()))
    if len(integer_list)==n:
        print(hash((integer_list)))