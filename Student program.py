students = []
age = []
id = []
course = []

#Register students with their age, ID, and course

def register(students, age, id, course):
    student_id = int(input("Id student: "))
    student_name = input("Student name: ")
    student_age = int(input("Age student: "))
    student_course = input("Student course: ")
    id.append(student_id)
    students.append(student_name)
    age.append(student_age)
    course.append(student_course)
    print("Successfully registered student")

#To view the registered students

def show_student_list():
    if len (students) == 0:
        print("There are no students registered")
        return
    print("Name list: ")
    for i in range(len(students)):
        print(f"ID: {id[i]} Student: {students[i]} Age: {age[i]} Course: {course[i]}")

#This is for searching for a student based on a specific criterion.

def Find_student():
    print("\n Search student")
    search = input("Enter name, age or ID: ")

    for i in range(len(students)):
        if (search == students[i]or
            search == str(age[i])or
            search == str(id[i])):
            print(f"ID: {id[i]} student: {students[i]} Course: {course[i]}")

#It would be to update a student

def update_student(): 
    print("Update a student's information: ")

    search_student = input("Enter id or student to update: ")
    for i in range(len(id)):
        if str(id[i]) == search_student:

            print("student found: ")
            print(f"ID {id[i]} Name: {students[i]} Age: {age[i]}")

            new_name = input("New name: ")
            new_age = input("New age: ")

            students[i] = new_name
            age[i] = new_age

            print("Student updated successfully.")
            break
        else:
            print("Student not finding.")


#It is allowed to remove a student

def delete_student():
    delete_id = input("Enter ID to delete: ")

    for i in range(len(id)):
        
        students.pop(i)
        age.pop(i)
        id.pop(i)

        print("Student deleted successfully")
        return
    print("Student not found")


print("Welcome to the menu")
while True:
    #Show menu for user 
    print("_"*40)
    print("\n  OPTIONS MENU   ")
    print("")
    print("1. Register new students. ")
    print("")
    print("2. Check the student list")
    print("")
    print("3. Find a student")
    print("")
    print("4. Update a student's information")
    print("")
    print("5. Eliminated student")
    print("")
    print("6. Leave")
    print("_"*40)

    option = input("Selection a option: ")

    # This is to register a student
    if option == "1":
        register(students, age, id, course)

    elif option == "2":
        show_student_list()

    
    elif option == "3":
        Find_student()
    
    elif option == "4":
        update_student()

    elif option == "5":
        delete_student()
    
    elif option == "6":
        print("Leaving...")
        break

    else: 
        print("invalidate option")
