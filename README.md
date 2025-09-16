![alt text](image.png)
# Not another SQL! Learn the basics of SQL queries

## Database Structure
- **students**: Stores 1,000 student records (id, first_name, last_name, age, grade).
- **courses**: Stores 1,000 course enrollments (course_id, course_name, student_id), with each student assigned exactly one course.

## Files
- `populate_students.py`: Inserts 1,000 student records with first and last names into the `students` table.
- `populate_courses.py`: Assigns one random course to each of the 1,000 students in the `courses` table.
- `sql_queries.ipynb`: Jupyter Notebook demonstrating SQL queries on the database.
- `demo.db`: SQLite database with `students` and `courses` tables.
- `docs/index.html`: GitHub Pages site.

## Running Queries in Jupyter
1. Install Jupyter: `pip install jupyter`
2. Run `populate_students.py` and `populate_courses.py` to set up the database.
3. Launch Jupyter: `jupyter notebook`
4. Open `queries.ipynb` to explore SQL queries.
