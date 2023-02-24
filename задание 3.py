from peewee import *

conn = SqliteDatabase('db_Student_2.sqlite')

class Students(Model):
    id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    surname = CharField(column_name='surname', max_length=32)
    age = IntegerField(column_name='age')
    city = CharField(column_name='city', max_length=32)

    class Meta:
        db_table = 'students'
        database = conn


class Courses(Model):
    id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name', max_length=32)
    time_start = CharField(column_name='time_start',max_length=8)
    time_end = CharField(column_name='time_end', max_length=8)

    class Meta:
        db_table = 'courses'
        database = conn

class Student_courses(Model):
    student_id = ForeignKeyField(Students, to_field='id')
    course_id = ForeignKeyField(Courses, to_field='id')

    class Meta:
        db_table = 'students_courses'
        database = conn

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

Students.create_table()
Students.insert_many(students_list)

Courses.create_table()
Courses.insert_many(courses_list)

Student_courses.create_table()
Student_courses.insert_many(students_courses_list)

def requests():
    req_1 = Students.select().where(Students.age > 30)
    print('req_1')
    for r_1 in req_1:
        print(r_1.id, r_1.name, r_1.surname)

    req_2= Students.select().join(Student_courses).join(Courses).where(Courses.name =='python')
    print('req_2')
    for r_2 in req_2:
        print(r_2.id, r_2.name, r_2.surname)

    req_3= Students.select().join(Student_courses).join(Courses).where((Courses.name =='python') & (Students.city == 'Spb'))
    print('req_3')
    for r_3 in req_3:
        print(r_3.id, r_3.name, r_3.surname)

print(requests())
