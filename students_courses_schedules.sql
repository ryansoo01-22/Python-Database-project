#give myself permissions to connect to server using python connector
#create user 'root'@'%' identified by 'S00m4n@33';
#grant all privileges on *.* to 'root'@'%' with grant option;
#flush privileges;

#CREATE DATABASE WITH TABLES
#create database if not exists students_courses_schedules; #creates database
#use students_courses_schedules;
#create table students (student_id int auto_increment primary key, first_name varchar(20), last_name varchar(20));
#create table classes (class_id int primary key, class_name varchar(255), class_time varchar(20));
#create table schedules (schedule_id int auto_increment primary key, student_id int, class_id int, day_of_week varchar(20), foreign key (student_id)
#references students (student_id), foreign key (class_id) references classes (class_id));

#ENROLL STUDENTS INTO PROGRAM
#insert into students (first_name, last_name) values ('ryan', 'soo');
#insert into students (first_name, last_name) values ('second_test2', 'second_test2');
#select * from students;

#INTRODUCE NEW CLASSES
#insert into classes (class_id, class_name, class_time) values (101, 'Math', '2 AM');
#insert into classes (class_id, class_name, class_time, days_of_week) values (200, 'Python', '11:00 AM', 'Tuesday, Thursday');
#select * from classes;

#ENROLL STUDENTS INTO CLASSES
#insert into schedules (student_id, class_id, day_of_week) values (1, 101, 'Monday');
#insert into schedules (student_id, class_id, day_of_week) values (1, 100, 'Wednesday');
#insert into schedules (student_id, class_id, day_of_week) values (1, 100, 'Friday');
#insert into schedules (student_id, class_id, day_of_week) values (2, 200, 'Tuesday');
#insert into schedules (student_id, class_id, day_of_week) values (2, 200, 'Thursday');
#select * from schedules;

#SEE SCHEDULE BASED ON STUDENT NAME
#select students.first_name, students.last_name, classes.class_name, classes.class_time, schedules.day_of_week from students 
#join schedules on students.student_id = schedules.student_id
#join classes on schedules.class_id = classes.class_id
#where students.first_name = 'ryan' and students.last_name = 'soo';

#VIEW WHICH STUDENTS ARE ENROLLED IN A CLASS
#select students.first_name, students.last_name from students 
#join schedules on students.student_id = schedules.student_id
#join classes on schedules.class_id = classes.class_id
#where classes.class_name = 'Math';

#VIEW STUDENT SCHEDULE BASED ON DAY
#select students.first_name, students.last_name, classes.class_name, classes.class_time from students
#join schedules on students.student_id = schedules.student_id
#join classes on schedules.class_id = classes.class_id
#where students.first_name = 'first_test1' and students.last_name = 'last_test1' and day_of_week = 'Wednesday';