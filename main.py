def menu():
    print("=" * 50)
    print(" * Welcome to student management system *")
    print("""
                       || Menu ||
                       1. Add Student Details.
                       2. Update.
                       3. Show all student.
                       4. Remove. 
    """)
    print("=" * 50)


student_DB = {'chetan': {'name': 'Chetan' , 'roll_no': 101 , 'Standard': 'first' , 'birth_year': 2000}}


def Add_student():
    student = {}
    s_name = input('enter student name you want to add :-')
    s_rollno = input('enter roll number :-')
    s_standard = input('enter standard :-')
    s_birthyear = input(' enter student birth year :-')

    student['name'] = s_name
    student['roll_no'] = s_rollno
    student['Standard'] = s_standard
    student['birth_year'] = s_birthyear

    student_DB[s_name] = student

    print(f"Student {s_name} is added successfully")
    print(student_DB)

def update_student():
    s_name = input('Enter student name you want to update :-')
    print(student_DB[s_name]['roll_no'])
    update_ip = eval(input(""" Enter your choice for update
                           1. Roll number
                           2. Standard
                           """))

    if update_ip == 1:
        s_roll_no = input("Enter updated roll number :- ")
        student_DB[s_name]['roll_no'] = s_roll_no

    elif update_ip == 2:
        s_standard = input("Enter updated Standard :- ")
        student_DB[s_name]['Standard'] = s_standard
    else:
        print("Invalid choice")

    print(f"Student {s_name} updated successfully")
    print(student_DB)



def show_student():
    for name in student_DB:
        print(student_DB[name])


def remove_student():
    s_name=input("Enter name of student you want to remove :-")
    del student_DB[s_name]
    print(f'Student {s_name} is successfully removed.')

while True:
    menu()
    get_ip = input('enter your preference as per menu :-')
    if (get_ip == '1'):
        Add_student()
    elif (get_ip == '2'):
        update_student()
    elif (get_ip == '3'):
        show_student()
    elif (get_ip == '4'):
        remove_student()
    else:
        print("you have enter invalid input")

    ch = input('Do you want to continue Y/N :-')
    ch=ch.lower()
    if (ch != 'y'):
        break
