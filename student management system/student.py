import os

FILE_NAME = "database.txt"


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{course},{marks}\n")

    print("Student added successfully!")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No student records available.")
        return

    print("\nStudent Records:")
    for student in students:
        data = student.strip().split(",")
        print(f"ID: {data[0]} | Name: {data[1]} | Age: {data[2]} | Course: {data[3]} | Marks: {data[4]}")


def search_student():
    search_id = input("Enter Student ID to search: ")

    with open(FILE_NAME, "r") as file:
        for student in file:
            data = student.strip().split(",")
            if data[0] == search_id:
                print(f"Student Found: {data}")
                return

    print("Student not found.")


def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            data = student.strip().split(",")
            if data[0] != delete_id:
                file.write(student)

    print("Student deleted if ID existed.")


def update_student():
    update_id = input("Enter Student ID to update: ")
    students = []

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            data = student.strip().split(",")
            if data[0] == update_id:
                print("Enter new details:")
                name = input("Name: ")
                age = input("Age: ")
                course = input("Course: ")
                marks = input("Marks: ")

                file.write(f"{update_id},{name},{age},{course},{marks}\n")
            else:
                file.write(student)

    print("Student updated if ID existed.")
def show_topper():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No records found.")
            return

        topper = None
        highest_marks = -1

        for student in students:
            data = student.strip().split(",")
            marks = int(data[4])

            if marks > highest_marks:
                highest_marks = marks
                topper = data

        print("\nTopper of the Class:")
        print(f"ID: {topper[0]} | Name: {topper[1]} | Course: {topper[3]} | Marks: {topper[4]}")

    except FileNotFoundError:
        print("Database not found.")
def average_marks():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No records found.")
            return

        total = 0
        count = 0

        for student in students:
            data = student.strip().split(",")
            total += int(data[4])
            count += 1

        avg = total / count

        print(f"\nAverage Marks of Class: {avg}")

    except FileNotFoundError:
        print("Database not found.")