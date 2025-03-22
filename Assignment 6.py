def display_menu():
    print("\nChoose an option:")
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. View one Student")
    print("4. View All Students")
    print("5. Exit")


def add_student(students):
    try:
        name = input("Enter student name: ")

        # Checking age input
        while True:
            try:
                age = int(input("Enter student age: "))
                if 0 <= age <= 120:  # Using  age range of 0 to 120
                    break
                print("Please enter a valid age between 0 and 120.")
            except ValueError:
                print("Please enter a valid number for age.")

        grade = input("Enter student grade: ")
        course = input("Enter student course: ")

        # Dictionary for storing Student Info.
        students[name] = {"age": age, "grade": grade, "course": course}
        print(f"{name} has been added to the system.")
    except Exception as e:
        print("An error occurred while adding the student. Please try again.")


def remove_student(students):
    if not students:
        print("No students in the system.")
        return

    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed from the system.")
    else:
        print(f"Student '{name}' not found in the system.")


def view_one_student(students):
    if not students:
        print("No students in the system.")
        return

    name = input("Enter student name to view: ")
    if name in students:
        student = students[name]
        print(f"\nStudent Details:")
        print(
            f"- {name}, Age: {student['age']}, Grade: {student['grade']}, Course: {student['course']}"
        )
    else:
        print(f"Student '{name}' not found in the system.")


def view_all_students(students):
    if not students:
        print("No students in the system.")
        return

    print("\nStudents in the system:")
    for name, details in students.items():
        print(
            f"- {name}, Age: {details['age']}, Grade: {details['grade']}, Course: {details['course']}"
        )


# Main Function to run Program


def main():
    print("Welcome to the Student Management System!")
    students = {}  # Dictionary to store student information

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice: ")

            if choice == "1":
                add_student(students)
            elif choice == "2":
                remove_student(students)
            elif choice == "3":
                view_one_student(students)
            elif choice == "4":
                view_all_students(students)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print("An error occurred. Please try again.")


if __name__ == "__main__":
    main()
