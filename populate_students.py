import sqlite3
import random

# List of sample first names (from your previous setup)
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Sophia", "Jackson", "Isabella", 
    "Lucas", "Mia", "Ethan", "Amelia", "Harper", "Evelyn", "Alexander", "Aria", 
    "James", "Charlotte", "Benjamin", "Luna", "Henry", "Sofia", "Daniel", "Avery", 
    "Michael", "Ella", "William", "Scarlett", "Logan", "Chloe", "David", "Penelope", 
    "Joseph", "Grace", "Samuel", "Victoria", "Owen", "Lily", "Gabriel", "Hannah", 
    "Matthew", "Julia", "Isaac", "Zoe", "Nathan", "Stella", "Jack", "Natalie", 
    "Ryan", "Mila", "Thomas", "Madison", "Dylan", "Addison", "Luke", "Layla", 
    "Christopher", "Zoey", "Andrew", "Nora", "Joshua", "Brooklyn", "Carter", "Leah", 
    "Sebastian", "Abigail", "Julian", "Emily", "Cameron", "Elizabeth", "Evan", "Sadie", 
    "Wyatt", "Violet", "Lincoln", "Claire", "Elijah", "Hazel", "Mason", "Ellie", 
    "Declan", "Skylar", "Caleb", "Katherine", "Isaiah", "Savannah", "Hunter", "Audrey", 
    "Levi", "Aubrey", "Jaxon", "Bella", "Grayson", "Lillian", "Jordan", "Lucy", "Janet",
    "Eli", "Paisley", "Zachary", "Anna", "Nicholas", "Caroline", "Aaron", "Tina", "Phil"
]

# List of common last names
last_names = [
    "Smith", "Anthony", "Cornelius", "Johnson", "Williams", "Brown", "Jones",  
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", 
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", 
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", 
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", 
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", 
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", 
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", 
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", 
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", 
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", 
    "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", 
    "Ross", "Foster", "Garcia", "Miller", "Davis", "Jimenez"
]

# Possible grades
grades = ['Fail', 'Credit', 'Distinction', 'High Distinction']

# Connect to the database
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# Drop and recreate the students table with a last_name column
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
''')

# Generate and insert 100 student records
random.seed(42)  # For reproducibility
for i in range(1000):
    first_name = random.choice(first_names)  # Randomly select first names
    last_name = random.choice(last_names)    # Randomly select last names
    age = random.randint(18, 45)             # Random age between 18 and 25
    grade = random.choice(grades)            # Random grade
    cursor.execute('''
        INSERT INTO students (first_name, last_name, age, grade) 
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, age, grade))

# Commit changes and close connection
conn.commit()
conn.close()

print("Inserted 1000 student records with first and last names into the students table!")