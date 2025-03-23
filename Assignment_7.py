# Simple Student Management System


def show_menu():
    print("\nWelcome to Student System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Show Grades")
    print("4. Show All Students")
    print("5. Exit")


def add_student(students):
    name = input("Enter student name: ")

    # Check if student exists
    if name in students:
        print("This student already exists!")
        return

    # Get age
    age = int(input("Enter student age: "))

    # Get grades
    subjects = {}
    print("\nAdd grades for subjects")
    while True:
        subject = input("Subject name (or press Enter to stop): ")
        if subject == "":
            if len(subjects) == 0:
                print("Add at least one subject!")
            else:
                break
        else:
            grade = float(input("Enter grade: "))
            subjects[subject] = grade

    # Calculate average
    total = 0
    count = 0
    for grade in subjects.values():
        total = total + grade
        count = count + 1
    average = total / count

    # Save student info
    student_info = {"age": age, "subjects": subjects, "average": average}
    students[name] = student_info

    print("Student added!")
    print("Grades:")
    for subject in subjects:
        print(f"{subject}: {subjects[subject]}")
    print(f"Average: {average}")


def update_student(students):
    if len(students) == 0:
        print("No students found!")
        return

    name = input("Enter student name: ")

    if name not in students:
        print("Student not found!")
        return

    print(f"\nCurrent info for {name}:")
    print(f"Age: {students[name]['age']}")
    print("Grades:")
    for subject in students[name]["subjects"]:
        print(f"{subject}: {students[name]['subjects'][subject]}")

    # Update info
    new_age = input("New age (press Enter to keep old age): ")
    if new_age != "":
        students[name]["age"] = int(new_age)

    # Update grades
    new_subjects = {}
    print("\nEnter new grades (press Enter to keep old grades)")
    while True:
        subject = input("Subject name (or press Enter to stop): ")
        if subject == "":
            if len(new_subjects) == 0:
                new_subjects = students[name]["subjects"]
            break
        else:
            grade = float(input("Enter grade: "))
            new_subjects[subject] = grade

    # Calculate new average
    total = 0
    count = 0
    for grade in new_subjects.values():
        total = total + grade
        count = count + 1
    new_average = total / count

    students[name]["subjects"] = new_subjects
    students[name]["average"] = new_average

    print("Student updated!")
    print("New grades:")
    for subject in new_subjects:
        print(f"{subject}: {new_subjects[subject]}")
    print(f"New average: {new_average}")


def show_grades(students):
    if len(students) == 0:
        print("No students found!")
        return

    print("\nStudent Grades:")
    print("-" * 40)

    for name in students:
        print(f"\nStudent: {name}")
        print(f"Age: {students[name]['age']}")
        print("Grades:")
        for subject in students[name]["subjects"]:
            print(f"{subject}: {students[name]['subjects'][subject]}")
        print(f"Average: {students[name]['average']}")
        print("-" * 40)

    # Calculate class average
    total = 0
    count = 0
    for student in students.values():
        total = total + student["average"]
        count = count + 1
    class_average = total / count
    print(f"\nClass Average: {class_average}")


def show_all_students(students):
    if len(students) == 0:
        print("No students found!")
        return

    print("\nAll Students:")
    print("-" * 40)

    for name in students:
        print(f"\nName: {name}")
        print(f"Age: {students[name]['age']}")
        print("Subjects and Grades:")
        for subject in students[name]["subjects"]:
            print(f"  {subject}: {students[name]['subjects'][subject]}")
        print(f"Average: {students[name]['average']}")
        print("-" * 40)


def main():
    students = {}

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            show_grades(students)
        elif choice == "4":
            show_all_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Wrong choice! Try again.")


main()
