import sqlite3
import random

# List of sample course names
course_names = [
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
    "History", "English Literature", "Economics", "Psychology", "Art"
]

# Connect to the database
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# Ensure the courses table exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        student_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
''')

# Clear existing courses (optional, remove if you want to append)
cursor.execute("DELETE FROM courses")

# Assign exactly one course to each student
random.seed(42)  # For reproducibility
for student_id in range(1, 1001):  # Students have IDs 1 to 1000
    course = random.choice(course_names)  # Select one random course
    cursor.execute('''
        INSERT INTO courses (course_name, student_id) 
        VALUES (?, ?)
    ''', (course, student_id))

# Commit changes and close connection
conn.commit()
conn.close()

print("Assigned one course to each of 1,000 students in the courses table!")