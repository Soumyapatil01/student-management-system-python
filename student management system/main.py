from student import add_student, view_students, search_student, delete_student, update_student, show_topper, average_marks

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Show Average Marks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            average_marks()

        elif choice == "8":
            print("Exiting program.")
            break

menu()