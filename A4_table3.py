# Question 3.....
#create database university****
import sqlite3

conn3 = sqlite3.connect('university.db')
#table3****
conn3.execute('''
Create Table faculty(
f_id Integer PRIMARY KEY AUTOINCREMENT,
f_name VARCHAR(100),
f_address VARCHAR(50),
f_phone VARCHAR(15),
f_mail VARCHAR(15)
)
''')
conn3.close()

#insertion...
import sqlite3
conn3 = sqlite3.connect("university.db")

conn3.execute('''
INSERT INTO faculty(f_id, f_name, f_address, f_phone, f_mail) VALUES (10, "arjun", "abc", "34566", "abc@123")
''')
conn3.commit()
conn3.close()