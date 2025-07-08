import sqlite3
# update operation perform on these three tables :

# update operation on table student :
conn1 = sqlite3.connect('university.db')
conn1.execute("""
UPDATE student 
SET phone = '123456' 
WHERE name = 'Riya'
""")
conn1.commit()
print("Student phone updated.")
conn1.close()


# update operation on table courses :
conn2 = sqlite3.connect('university.db')
conn2.execute("""
UPDATE courses 
SET cost = '4500' 
WHERE c_name = 'B_tech'
""")
conn2.commit()
print("Course cost updated.")
conn2.close()


# update operation on table faculty :
conn3 = sqlite3.connect('university.db')
conn3.execute("""
UPDATE faculty 
SET f_mail = 'vikram@updated.com' 
WHERE f_name = 'Vikram'
""")
conn3.commit()
print("Faculty email updated.")
conn3.close()
