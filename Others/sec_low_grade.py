if __name__ == '__main__':
    n = int(input())  # Number of students
    students = []  # List to store (name, grade) tuples

    for _ in range(n):
        name = input()
        grade = float(input())
        students.append((name, grade))

    # Sort by grade first, then by name (automatically sorts by name if grades are equal)
    students.sort(key=lambda x: x[1])

    # Extract unique grades and find the second lowest one
    unique_grades = sorted(set(grade for _, grade in students))
    second_lowest_grade = unique_grades[1]  # Second lowest

    # Get all names with the second lowest grade
    second_lowest_students = sorted([name for name, grade in students if grade == second_lowest_grade])

    # Print names in separate lines
    for student in second_lowest_students:
        print(student)
