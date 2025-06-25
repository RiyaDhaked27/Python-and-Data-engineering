# ********************************* Assignment_5 *******************************
import pandas as pd

# ...................question 1.........
# part(a)......
data_set = {"digits":[10,20,30,40],
            "alpha":['a','b','c','d']
            }
df = pd.Series(data_set)
print(df)

# part(b)......
a = [1,7,3,4,6]
s = pd.Series(a)                 #pandas series
print(s)

# part(c)...........
a = [1,7,3,4,6]
s = pd.Series(a)
res = s.iloc[2]
print(res)

# ...................question 2.........
#part(a)...........
data = [[1,'Abhay'], [2,'Riya'], [3,'Bhumi']]
df = pd.DataFrame(data, columns=['col1', 'col2'], index=['a.', 'b.', 'c.'])
print(df)

# part(b)..........
data_dic = {"Roll no.": [1,2,3], "Name": ['Abhay', 'Riya', 'Bhumi']}
df_d = pd.DataFrame(data_dic,  index=['a.', 'b.', 'c.'])
print(df_d)

# part(c)............
data_list = [['Python', '4500/-'], ['Web development', '2000/-'], ['DSA', '4000/-']]
df_l = pd.DataFrame(data_list, columns=['courses', 'cost'], index=['a.', 'b.', 'c.'])
print(df_l)

# part(d)............
data_tuple = [(10, 'Arjun', 45678), (20, 'Vikram', 23450), (30, 'Riya', 58698)]
df_t = pd.DataFrame(data_tuple, columns=['id', 'Name', 'phone'], index=['a.', 'b.', 'c.'])
print(df_t)

# part(e)............
data = [{'id': 1, 'name': 'Riya'}, {'id': 2, 'name': 'Rahul'}, {'id': 3, 'name': 'Bhumi'}]
df = pd.DataFrame(data)
print(df)

# ............Question 3..........
#part(a)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['Riya', 'Rahul']})

# Using iterrows()
for index, row in df.iterrows():
    print(f"Row {index}: id={row['id']}, name={row['name']}")

# Using itertuples()
for row in df.itertuples():
    print(f"id={row.id}, name={row.name}")

# part(b)...........
df = pd.DataFrame({'id': [1, 2, 3], 'marks': [90, 70, 85]})

# Select rows where marks > 80
high_marks = df[df['marks'] > 80]
print(high_marks)

# part(c)...........
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Riya', 'Rahul', 'Abhay']})

# Select the second row (index 1)
print(df.iloc[1])
print(df.iloc[1, 0])          #print element of second(index 1) row and first(index 0) column

# part(d)...........
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['Riya', 'Rahul', 'Abhay']})

# Show first 2 rows of 'name' column
df_row = df.iloc[0:2, 1]
print(df_row)            #print(df.loc['name']) is incorrect

#part(e)...........
df = pd.DataFrame({'id': [1, 2, 3], 'marks': [90, 60, 75]})

# Drop rows which contain marks = 75
df = df[df['marks'] != 75]
print(df)

#part(f)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['Riya', 'Rahul']})

# New row to insert
new_row = pd.DataFrame({'id': [3], 'name': ['Abhay']})

# Insert at position 1
df = pd.concat([df.iloc[:1], new_row, df.iloc[1:]]).reset_index(drop=True)
print(df)

#part(g)...........
df = pd.DataFrame({'id': [1, 2], 'name': ['Riya', 'Rahul']})

# Convert each row to a list
row_list = df.values.tolist()
print(row_list)





