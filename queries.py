import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# Query 1: Select all students
print("All Students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Query 2: Select students with grade 'A'
print("\nStudents with High Distinction:")
cursor.execute("SELECT first_name, last_name, age FROM students WHERE grade = 'High Distinction'")
for row in cursor.fetchall():
    print(row)

# Query 3: Join students and courses (update if courses table exists)
print("\nStudents and Their Courses:")
cursor.execute('''
    SELECT students.first_name, students.last_name, courses.course_name
    FROM students
    JOIN courses ON students.id = courses.student_id
''')
for row in cursor.fetchall():
    print(row)

conn.close()