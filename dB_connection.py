import mysql.connector

# def db_connection():
#     con = mysql.connector.connect(
#         host="localhost" ,
#         user="root" ,
#         password="Chetan@05" ,
#         auth_plugin='mysql_native_password'
#     )
#     print(con)

def add_student():
    con = mysql.connector.connect(
        host="localhost" ,
        user="root" ,
        password="Chetan@05" ,
        auth_plugin='mysql_native_password',
        database = "students"
    )
    print(con)
    cursor = con.cursor()
    name = input("Enter Student Name: ")
    marks = float(input("Enter Student Marks: "))
    roll_no = int(input("Enter Student Roll Number: "))
    query = f""" INSERT INTO student_info (name , marks , roll_no) 
                        values('{name}' , {marks} , {roll_no}) """
    cursor.execute(query)
    con.commit()

add_student()