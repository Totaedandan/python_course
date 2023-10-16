class Student:
    def __init__(self, id, name, test_score):
        self.id = id
        self.name = name
        self.test_score = test_score


def main():
    students = []

    while True:
        print("Menu:")
        print("1 - Add student")
        print("2 - Manage records")
        print("3 - Calculate grades")
        print("4 - View statistics")
        print("5 - Generate reports")
        print("6 - Delete student")
        print("7 - Logout and exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter student name: ")
            id = int(input("Enter student ID: "))
            test_score = float(input("Enter test score: "))
            students.append(Student(id, name, test_score))

        elif choice == '2':
            update_id = int(input("Enter student ID to update score: "))
            found = False
            for student in students:
                if student.id == update_id:
                    new_score = float(input("Enter new test score: "))
                    student.test_score = new_score
                    found = True
                    break
            if not found:
                print("Student not found.")

        elif choice == '3':
            print("Grades calculated.")

        elif choice == '4':
            if not students:
                print("No students to calculate statistics.")
            else:
                total_students = len(students)
                sum_scores = sum(student.test_score for student in students)
                average_score = sum_scores / total_students
                highest_score = max(student.test_score for student in students)
                lowest_score = min(student.test_score for student in students)
                print("Total students:", total_students)
                print("Average score:", average_score)
                print("Highest score:", highest_score)
                print("Lowest score:", lowest_score)

        elif choice == '5':
            print("No reports.")

        elif choice == '6':
            delete_id = int(input("Enter student ID to delete: "))
            for student in students:
                if student.id == delete_id:
                    students.remove(student)
                    print("Student with ID", delete_id, "deleted.")
                    break

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-7).")


if __name__ == "__main__":
    main()
