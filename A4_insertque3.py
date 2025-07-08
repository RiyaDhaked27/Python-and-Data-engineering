import sqlite3

#*****************insertion in table no. 1 ******************
conn1 = sqlite3.connect('university.db')

conn1.execute('''
INSERT INTO student(name, address, phone, mail_id) VALUES ("Riya", "jaipur", "274758", "riya@123")
''')
conn1.execute('''
INSERT INTO student(name, address, phone, mail_id) VALUES ("Rahul", "odisha", "847596", "rahul@348")
''')
conn1.execute('''
INSERT INTO student(name, address, phone, mail_id) VALUES ("Abhay", "USA", "9684749", "abhay@567")
''')
conn1.commit()
conn1.close()

#*****************insertion in table no. 2 ******************
conn2 = sqlite3.connect('university.db')

conn2.execute('''
INSERT INTO courses(c_name, cost, duration) VALUES ("B_tech", "4000", "4yr.")
''')
conn2.execute('''
INSERT INTO courses(c_name, cost, duration) VALUES ("M_tech", "8000", "5yr.")
''')
conn2.execute('''
INSERT INTO courses(c_name, cost, duration) VALUES ("MBA", "10000", "4yr.")
''')
conn2.commit()
conn2.close()

#******************insertion in table no. 3 ******************
conn3 = sqlite3.connect('university.db')

conn3.execute('''
INSERT INTO faculty(f_name, f_address, f_phone, f_mail) VALUES ("Arjun", "abc", "34566", "abc@123")
''')
conn3.execute('''
INSERT INTO faculty(f_name, f_address, f_phone, f_mail) VALUES ("Vikram", "bcd", "96759", "bdc@567")
''')
conn3.execute('''
INSERT INTO faculty(f_name, f_address, f_phone, f_mail) VALUES ("Drishti", "rts", "45678", "bmn@965")
''')
conn3.commit()
conn3.close()
