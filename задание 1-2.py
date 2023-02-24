#задание 1
import sqlite3
conn = sqlite3.connect('db_sudent.sqlite3')
cursor = conn.cursor()

students =('''CREATE TABLE IF NOT EXISTS Students (
               id int PRIMARY KEY,
               name Varchar(32),
               surname Varchar(32),
               age int,
               city Varchar(32))''')

courses =('''CREATE TABLE IF NOT EXISTS Courses (
                id int PRIMARY KEY ,
                name Varchar(32),
                time_start data char(8),
                time_end data char(8))''')

student_courses =('''CREATE TABLE IF NOT EXISTS Student_courses (
               student_id int ,
               course_id int,
               FOREIGN KEY (student_id) REFERENCES Student(id),
               FOREIGN KEY (course_id)REFERENCES Courses(id))''')

cursor.execute(students)
cursor.execute(courses)
cursor.execute(student_courses)


#задание 2
students_list = [(1, 'Max', 'Brooks', 24, 'Spb'),
                 (2, 'John', 'Stones', 15, 'Spb'),
                 (3, 'Andy', 'Wings', 45, 'Manhester'),
                 (4, 'Kate', 'Brooks', 34, 'Spb')]

courses_list = [(1, 'python', '21.07.21', '21.08.21'),
                (2, 'java', '13.07.21', '16.08.21')]

students_courses_list = [(1,1),
                         (2,1),
                         (3,1),
                         (4,2)]

cursor.executemany("INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?)", students_list)
cursor.executemany("INSERT OR IGNORE INTO Courses VALUES (?, ?, ?, ?)", courses_list)
cursor.executemany("INSERT OR IGNORE INTO Student_courses VALUES (?, ?)",students_courses_list)
conn.commit()

r1 = cursor.execute("SELECT name, surname FROM Students WHERE age > 30")
print(r1.fetchall())

r2 = cursor.execute('''SELECT Students.name, Students.surname FROM  Students 
                    JOIN Student_courses ON Student_courses.student_id = student_id
                    JOIN Courses ON Student_courses.course_id = course_id
                    WHERE Courses.name = "python"''')
print(r2.fetchall())

r3 = cursor.execute('''SELECT Students.name, Students.surname FROM  Students 
                    JOIN Student_courses ON Student_courses.student_id = student_id
                    JOIN Courses ON Student_courses.course_id = course_id
                    WHERE Courses.name = "python" AND Students.city = "Spb"''')
print(r3.fetchall())
conn.close()