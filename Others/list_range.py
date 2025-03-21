if __name__ == '__main__':
    l=[]
    n = int(input())
    for i in range(n):
        command=input().split()
        cmd=command[0]
        
        if cmd=="insert":
            l.insert(int(command[1]),int(command[2]))
        elif cmd=="print":
            print(l)
        elif cmd=="remove":
            l.remove(int(command[1]))
        elif cmd=="append":
            l.append(int(command[1]))
        elif cmd=="sort":
            l.sort()
        elif cmd=="pop":
            l.pop()
        elif cmd=="reverse":
            l.reverse()