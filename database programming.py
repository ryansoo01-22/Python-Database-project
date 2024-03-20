import mysql.connector

host = 'COMPUTER NAME'
user = 'root'
password = 'PASSWORD'
port = '3306'
database = 'YOUR SCHEMA NAME'

# Create the initial connection and cursor
connection = mysql.connector.connect(host=host, user=user, password=password, port=port)
cursor = connection.cursor()

if connection.is_connected():
    print("connected!")

# Create the database if it doesn't exist
create_db_query = 'CREATE DATABASE IF NOT EXISTS students_courses_schedules;'
use_db_query = 'USE students_courses_schedules;'
create_students = 'CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20));'
create_classes = 'CREATE TABLE IF NOT EXISTS classes (class_id INT PRIMARY KEY, class_name VARCHAR(255), class_time VARCHAR(20), class_days VARCHAR(500));'
create_schedules = 'CREATE TABLE IF NOT EXISTS schedules (schedule_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, class_id INT, day_of_week VARCHAR(20), FOREIGN KEY (student_id) REFERENCES students (student_id), FOREIGN KEY (class_id) REFERENCES classes (class_id));'

# Execute queries
cursor.execute(create_db_query)
cursor.execute(use_db_query)
cursor.execute(create_students)
cursor.execute(create_classes)
cursor.execute(create_schedules)

# Commit changes
connection.commit()

welcome = "Welcome to Ryan Soo's SWE 243 project. \n You can add new students to the program, add courses to the curriculum, and enroll students in courses. \
    \n Please select what you would like to do from the menu \n1. enroll student in program \n2. add course to curriculum \n3. enroll student into a course \
    \n4. See which students are in each course \n5. See what courses each student is in \n6. See what courses and what times each course is for a given student on a given day of the week. \n Enter Q to quit.\n"

menu =  'Please select what you would like to do from the menu \n1. enroll student in program \n2. add course to curriculum \n3. enroll student into a course \
    \n4. See which students are in each course \n5. See what courses each student is in \n6. See what courses and what times each course is for a given student on a given day of the week. \n Enter Q to quit.\n'

def get_all_students():
    select_query = 'select * from students'
    cursor.execute(select_query)
    result = cursor.fetchall()
    return result

def get_all_classes():
    select_query = 'select * from classes'
    cursor.execute(select_query)
    result = cursor.fetchall()
    return result

def add_student(first_name, last_name):
    insert_query = 'insert into students (first_name, last_name) values (%s, %s)'
    cursor.execute(insert_query, (first_name, last_name))
    connection.commit()
    print("You have just enrolled {} {} into the program!\n".format(first_name, last_name))

def add_course(class_id, class_name, class_time, class_days):
    insert_query = 'insert into classes (class_id, class_name, class_time, class_days) values (%s, %s, %s, %s)'
    cursor.execute(insert_query, (class_id, class_name, class_time, class_days))
    connection.commit()
    print("You have just added the course {}\n".format(class_name))

def get_student_id(first_name, last_name):
    select_query = 'select student_id from students s where s.first_name = %s and s.last_name = %s'
    cursor.execute(select_query, (first_name, last_name))
    result = cursor.fetchall()
    return result

def enroll_student(student_id, class_id):
    insert_query = 'insert into schedules (student_id, class_id) values (%s, %s)'
    cursor.execute(insert_query, (student_id, class_id))
    connection.commit()
    print("You have just enrolled the student in a class!\n")

def format_student_schedule(rows, fname, lname):
    output = "\n%s %s's schedule\n________________________\n" % (fname, lname)
    for i in rows:
        for j in i[4].split(' '):
            output += "Class: " + i[2] + " Time: " + i[3] + " Days: " + j + '\n'
    return output

def see_student_schedule(first_name, last_name):
    select_query = 'select students.first_name, students.last_name, classes.class_name, classes.class_time, classes.class_days from students \
    join schedules on students.student_id = schedules.student_id \
    join classes on schedules.class_id = classes.class_id \
    where students.first_name = %s and students.last_name = %s;'
    cursor.execute(select_query, (first_name, last_name))
    result = cursor.fetchall()
    print(format_student_schedule(result, first_name, last_name))

def get_student_schedule_ID(first_name, last_name):
    select_query = 'select students.first_name, students.last_name, classes.class_id, classes.class_time, classes.class_days from students \
    join schedules on students.student_id = schedules.student_id \
    join classes on schedules.class_id = classes.class_id \
    where students.first_name = %s and students.last_name = %s;'
    cursor.execute(select_query, (first_name, last_name))
    result = cursor.fetchall()
    return result

def format_class_students(rows, class_name):
    output = '\nStudents enrolled in %s\n___________________________________\n' % class_name
    for i in rows:
        output += i[0] + " " + i[1] + '\n'
    return output

def see_class_students(class_name):
    select_query = 'select students.first_name, students.last_name from students \
    join schedules on students.student_id = schedules.student_id \
    join classes on schedules.class_id = classes.class_id \
    where classes.class_name = %s;'
    cursor.execute(select_query, [class_name])
    result = cursor.fetchall()
    print(format_class_students(result, class_name))

def format_day_schedule(rows, fname, lname, day):
    output = "\n%s %s's schedule on %s\n___________________\n" % (fname, lname, day)
    if not rows:
        output += "NO CLASSES ON %s WOOHOO!\n"
        return output
    for i in rows:
        output += "Class: %s Time: %s\n" % (i[2], i[3])
    return output 

def see_student_day_schedule(first_name, last_name, day):
    select_query = 'select students.first_name, students.last_name, classes.class_name, classes.class_time from students \
    join schedules on students.student_id = schedules.student_id \
    join classes on schedules.class_id = classes.class_id \
    where students.first_name = %s and students.last_name = %s;'
    cursor.execute(select_query, (first_name, last_name))
    result = cursor.fetchall()
    print(format_day_schedule(result, first_name, last_name, day))

def get_student_id(first_name, last_name):
    select_query = 'select student_id from students s where s.first_name = %s and s.last_name = %s;'
    cursor.execute(select_query, (first_name, last_name))
    result = cursor.fetchall()
    return result[0][0]

running = input(menu)
while running != 'Q':
    if running == '1':
        prompt = "You chose to add a student. Please enter the first and last name of the student when prompted."
        print(prompt)
        all_students = get_all_students()
        first = input('First name: ')
        last = input('Last name: ')
        if all_students:
            for i in all_students:
                if first in i and last in i:
                    print("That student is already enrolled in the program!\n")
                    break
                else:
                    add_student(first, last)
        else:
            add_student(first, last)
        
    if running == '2':
        prompt = "You chose to add a course to the curriculum. Please enter in the class id, class name, and class days when prompted"
        print(prompt)
        class_id = input('Class id: ')
        class_name = input('Class name: ')
        class_time = input('Class time: ')
        class_days = input('Class days(separate the days by spaces): ')
        all_classes = get_all_classes()
        if all_classes:
            for i in all_classes:
                if class_id in i and class_name in i and class_time in i and class_days in i:
                    print("That course is already offered in the program!\n")
                    break
                else:
                    add_course(class_id, class_name, class_time, class_days)
        else:
            add_course(class_id, class_name, class_time, class_days)
    
    if running == '3':
        prompt = "You chose to enroll a student in a class. Please enter in the student's first name, last name, and the class_id when prompted"
        print(prompt)
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        student_id = get_student_id(first_name, last_name)
        class_id = input('Class id: ')
        student_schedule = get_student_schedule_ID(first_name, last_name)
        if len(student_schedule) >= 1:
            for i in student_schedule:
                if int(class_id) in i:
                    print("That student is already enrolled in the class!\n")
                    break
                else:
                    enroll_student(student_id, class_id)
                    print("You have enrolled %s %s in %s!", first_name, last_name, class_id)
        else:
            print("ENROLLING STUDENT")
            enroll_student(student_id, class_id)

    if running == '4':
        prompt = "You chose to see which students are enrolled in a class. Please enter the class name for the student list you want to see when prompted"
        print(prompt)
        class_name = input('Class name: ')
        see_class_students(class_name)
        
    
    if running == '5':
        prompt = "You chose to see a student's class schedule. Please enter in the student's first and last name when prompted"
        print(prompt)
        first_name = input('First name: ')
        last_name = input('Last name: ')
        see_student_schedule(first_name, last_name)
    
    if running == '6':
        prompt = "You chose to see a student's schedule for a certain day. Please enter the first and last name and day of the week you want to see when prompted"
        print(prompt)
        first_name = input('First name: ')
        last_name = input('Last name: ')
        day_of_week = input("Day of the week: ")
        see_student_day_schedule(first_name, last_name, day_of_week)

    running = input(menu)

# Close the cursor and connection when done
cursor.close()
connection.close()
