import sqlite3

# Deletion operation perform on these three tables :
# (we can use connection name same or differ that is conn or conn1,2,3)

# deletion on table student :
conn = sqlite3.connect('university.db')
conn.execute("""
DELETE FROM student 
WHERE name = 'Abhay'
""")
conn.commit()
print("Abhay's record deleted from student table.")
conn.close()

# deletion on table courses :
conn = sqlite3.connect('university.db')
conn.execute("""
DELETE FROM courses 
WHERE c_name = 'MBA'
""")
conn.commit()
print("MBA course deleted.")
conn.close()

# deletion on table faculty :
conn = sqlite3.connect('university.db')
conn.execute("""
DELETE FROM faculty 
WHERE f_name = 'Drishti'
""")
conn.commit()
print("Drishti's record deleted from faculty table.")
conn.close()
