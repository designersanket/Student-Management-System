student_grades={}
def add_student(name,grade):
    student_grades[name]=grade
    print(f"Student name {name} and {grade} added successfully.")

def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"Student name {name} and {grade} updated successfully.")
    else:
        print(f"Name {name} of student is not found.")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student {name} details deleted successfully.")
    else:
        print(f"student name {name} not found.")

def view_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("Student not found.")

def main():
    while True:
        print("1.Add Student details.\n 2.Updat student\n 3.Delete Student details\n 4.View all student.\n 5.Exit.")
        user_choice=int(input("Enter your choice:"))

        if user_choice==1:
            name=input("Enter name for student:")
            grade=input("Enter stident grade:")
            add_student(name,grade)

        elif user_choice==2:
            name=input("Enter student name:")
            grade=input("Enter student  grade:")
            update_student(name,grade)

        elif user_choice==3:
            delete_student(name)

        elif user_choice==4:
            view_all_student()

        elif user_choice==5:
            print("Student Grade management system is exiting...")
            break
        else:
            print("Invalid choice.")


if __name__=='__main__':    
    print("Wellcome to Student Grade Management System.")                        
    main()