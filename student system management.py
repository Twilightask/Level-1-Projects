print('Welcome to Student Management System')

student = {}

def add_stud():            #To add new student info 
    name = input("Enter name:")
    rollno = int(input("Enter Roll no:"))
    std = int(input("Enter standard:"))
    div = input("Enter DIVISION:")
    print("Information entered successfully")
    
    student[rollno] = {
        "Name": name, 
        "Division": div, 
        "Std": std
    }
    
def view_student():        #To view all student 
    if not student:
        print("No student found")
    else:
        for rollno,info in student.items():
            print("ROLL NO.",rollno)
            print("Name:", info["Name"])
            print("Std:", info["Std"])
            print("Div:", info["Division"])
    
def search_student():     #To search a single student
    rollno = int(input("Enter rollno of student: "))
    if rollno in student:
        for rollno,info in student.items():
            print("ROLL NO.",rollno)
            print("Name:", info["Name"])
            print("Std:", info["Std"])
            print("Div:", info["Division"])
    else:
        print("Student not found")

def delete_stud():       #To delete a student data
    rollno = int(input("Enter student rollno: "))
    if rollno in student:
        del student[rollno]
        print("Student deleted")
    else:
        print("Student not found")
        
def exit_app():       #To exit the program
    print("Thank you")
    

while True:
    print('\n1.Add new student info \n2.View student list \n3.Search for a student \n4.Delete a student \n5.Exit the app')
    choice = int(input("Enter choice number: "))
    
    if choice == 1:
        add_stud()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_stud()
    elif choice == 5:
        exit_app()
        break
    else:
        print("Please enter a correct choice")
    
    
    
    
    
    

    

