# broadly
if __name__ == '__main__':
    n = int(input("enter range: "))
    student_marks = {}
    students_avg={}
    for _ in range(n):
        name, *line = input("enter name: ").split()
        scores = list(map(float, line))
        student_marks[name]=scores
        print(student_marks)
        students_avg[name] = sum(scores)/len(scores)
        print(students_avg)
    query_name = input()
    print(f"{students_avg[query_name]:.2f}")
    
# briefly
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/len(scores)
    query_name = input()
    print(f"{student_marks[query_name]:.2f}")