import sqlite3
db_file = "mysports.db."

db = sqlite3.connect(db_file)
cursor = db.cursor()
sql_query = "SELECT * \
		   FROM emp"
cursor.execute(sql_query)
all_emp_rows = cursor.fetchall()
for emp_row in all_emp_rows:
    print(emp_row)
db.close()
