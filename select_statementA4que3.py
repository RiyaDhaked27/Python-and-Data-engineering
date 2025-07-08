import sqlite3
# for showing on compiler
#***************** print insertion data in table no. 1 ******************
conn1 = sqlite3.connect('university.db')

data = conn1.execute("select * from student")
for x in data:
    print("\ndata of student table:\n",x)
conn1.close()

#***************** print insertion data in table no. 2 ******************
conn2 = sqlite3.connect('university.db')

data = conn2.execute("select * from courses")
for x in data:
    print("\ndata of courses table:\n", x)
conn2.close()

# ***************** print insertion data in table no. 3 ******************
conn3 = sqlite3.connect('university.db')

data = conn3.execute("select * from faculty")
for x in data:
    print("\ndata of faculty table:\n",x)
conn3.close()