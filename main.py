import json

def load_students():
    try:
        with open("students.json","r")as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    
def save_students(students):
    with open("students.json","w") as file:
        json.dump(students, file, indent=0)



def show_menu():
    
    # print("1. Add Student")
    # print("2. Show Student")
    # print("3. Search Student")
    # print("4. Delete Student")
    # print("5. Exit")
    while True:
        print("1. Add Student")
        print("2. Show Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            print("Please Enter valid input: ")
        

def add_student(students):
    
    name = input("Enter the name of student: ")
    while True:
        try:
            roll_number = int(input("Enter the Roll Number: "))
        
            found = False
            for student in students:
                if student["Roll Number"] == roll_number:
                    print("Already exists")
                    found = True
                    break
            if found:
                continue
                        
        except ValueError:
            print("Please enter value in number: ")
            continue
        try:
            age = int(input("Enter the age of student: "))
            break
        except ValueError:
            print("Please enter value in number: ")
            continue

    student = {
        "Name" : name,
        "Roll Number": roll_number,
        "Age" : age 

    }
    return student

students = load_students()
def search_student(students):
    while True:
        try:
            search = int(input("Enter the student you want to search: "))
            break
        except ValueError:
            print("Please enter integer value")
            continue
    found = False

    for index ,student in enumerate(students,start=1):
        if student["Roll Number"] == search:
            print(f"Student {index}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll Number']}")
            print(f"Age: {student['Age']}")
            print("-"*30)
            found = True
    if not found:
        print("Not found any student")  
def delete_student(students):
    while True:
        try:
            del_student = int(input("Enter the Roll Number of the student: "))
            break
        except ValueError:
            print("Please Enter a Valid Value.")

    found = False

    for student in students:
        if student["Roll Number"] == del_student:
            students.remove(student)
            found = True
            save_students(students)
            print("Student deleted successfully.")
            return

    if not found:
        print("Student not found.")    
def update_student(students):
    while True:
        try:
            find_student = int(input("Please enter the student Roll No: "))
            break
        except ValueError:
            print("Enter Roll Number in integer formate")
            continue
    
    found = False
    for student in students:
        if student["Roll Number"] == find_student:
            found = True
            print(f"Name: {student['Name']}")
            user_choice = None
            while True:
                new_name = input("Enter New Name (Press Enter to keep the current name):")
                if new_name == "":
                    
                    while True:
                        print("You entered an empty name.") 
                        new_name_check = input("Do you want to keep the current name? (Y/N): ").upper()
                        if new_name_check == "N":

                            break
                        elif new_name_check == "Y":
                            user_choice = "Y"
                            break
                        
                        else:
                            print("Please Enter only Y or N")
                    if user_choice == "Y":
                        break
                else:
                    student["Name"] = new_name
                    break
            age_choice = None
            while True:
                print(student["Age"])
                try:
                    new_age = int(input("Enter new age: "))
                except ValueError:
                    print("Please enter a valid value")
                    continue
                if student["Age"] == new_age:
                    while True:
                        print("You enter the old age.")
                        old_age_check = input("Do you want to keep the old age? Y/N: ").upper()
                        if old_age_check == "N":
                            break
                        elif old_age_check == "Y":
                            age_choice = "Y"
                            break
                    if age_choice == "Y":
                        break
                elif new_age < 0:
                    print("Please enter Age is positive number.")
                    continue
                # elif new_age > 0:
                #     try:
                #         student["Age"] = new_age
                #     except ValueError:
                #         print("Please enter age as integer.")
                #         continue
                else:
                    student["Age"] = new_age
                    break
            save_students(students)
            print("Student updated successfully.")
            
    if not found:
        print("Student Not found")

while True:
    choice = show_menu()

    if choice == 1:
        new_student = add_student(students)
        students.append(new_student)
        save_students(students)
        
    elif choice == 2:

        print(f"\n=======Show Students========")
        for index,student in enumerate(students,start=1):
            print(f"Student {index}")
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll Number']}")
            print(f"Age: {student['Age']}")
            print("-"*30)

    elif choice == 3:
        search_student(students)
    elif choice == 4:
        delete_student(students)
    elif choice == 5:
        update_student(students)
    elif choice == 6:
        print("Thank you for using Student Management System.")
        break