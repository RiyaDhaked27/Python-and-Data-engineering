import sqlite3

#table2****
conn2 = sqlite3.connect('university.db')
conn2.execute('''
Create Table courses(
id Integer PRIMARY KEY AUTOINCREMENT,
c_name VARCHAR(100),
cost VARCHAR(50),
duration VARCHAR(15)
)
''')
conn2.close()

#insertion...
import sqlite3
conn2 = sqlite3.connect("university.db")

conn2.execute('''
INSERT INTO courses(id, c_name, cost, duration) VALUES (100, "b_tech", "4000", "1yr.")
''')
conn2.commit()
conn2.close()