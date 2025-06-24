# Question 3.....
#create database university****(table1)
import sqlite3

conn1 = sqlite3.connect('university.db')
#table1****
conn1.execute('''
Create Table student(
id Integer PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100),
address VARCHAR(50),
phone VARCHAR(15),
mail_id VARCHAR(15)
)
''')
conn1.close()

#insertion.....
import sqlite3
conn1 = sqlite3.connect("university.db")

conn1.execute('''
INSERT INTO student(id, name, address, phone, mail_id) VALUES (1, "Riya", "jaipur", "274758", "riya@123")
''')
conn1.commit()
conn1.close()