
students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []

    print("\nStudent", i + 1)

    for j in range(subjects):
        mark = float(input("Enter marks: "))
        row.append(mark)

    marks.append(row)

print("\n----- STUDENT MARKS REPORT -----")

for i in range(students):
    total = 0

    for j in range(subjects):
        total = total + marks[i][j]

    average = total / subjects

    print("Student", i + 1)
    print("Total marks:", total)
    print("Average marks:", average)

print("\n----- SUBJECT AVERAGES -----")

for j in range(subjects):
    total = 0

    for i in range(students):
        total = total + marks[i][j]

    average = total / students

    print("Subject", j + 1, "Average:", average)
