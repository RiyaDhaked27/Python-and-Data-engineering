# ************************************ Assignment 7 *********************************************
#                                     --------------
import pandas as pd
import numpy as np

# >>>>>>>>>>>>>>>>>> Question 1 >>>>>>>>>>>>>>>>>>>>>>
#extract only digits from string :
df = pd.DataFrame(['abc123xyz', '456hello789'], columns=['value'])
df['digits'] = df['value'].str.replace(r'\D+', '' ,regex=True)            #\D matches any character that is not a decimal digit
print("only digits are:\n",df)

#extract only alphabets from string :
df = pd.DataFrame(['abc123', '456Hello'], columns=['value'])
df['alphabets'] = df['value'].str.replace(r'[^a-zA-Z]+', '', regex=True)    #[^a-zA-Z] matches only alphabets that is not any digits
print("only alphabets are:\n",df)

# remove special character from string :
df = pd.DataFrame(['Hello@World!', 'Welcome#2025'], columns=['text'])
df['col'] = df['text'].str.replace(r'[^\w\s]+', '', regex=True)             #[^\w\s] use for removing special character
print("after removing special character:\n", df)

# extract indian mobile number :
df = pd.DataFrame(['Call 9876543210 now', 'Alt: 9123456789'], columns=['text'])
df['mobile no.'] = df['text'].str.extract(r'([6-9]\d{9})')                 # +', '', regex=True not use in extract() syntax
print("indian mobile number is:\n", df)

# extract valid email address :
df = pd.DataFrame(['Contact us at riya123@example.com for info.'], columns=['text'])
df['email'] = df['text'].str.extract(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
print("valid email address:\n", df)


# >>>>>>>>>>>>>>>>>> Question 2 >>>>>>>>>>>>>>>>>>>>>>
# use datetime() function :
df = pd.DataFrame({'date': ['2025-06-26', '2024-12-01']})
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)

# get Date Parts (Year, Month, Day, etc.):
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.day_name()
print(df)

# >>>>>>>>>>>>>>>>>> Question 3 >>>>>>>>>>>>>>>>>>>>>>
df = pd.read_csv("people-100.csv")
print(df)
# use to_string for print entire dataframe
print(df.to_string())

print(df.head(10))          # # print starting 10 entries
print(df.tail(10))          # print last 10 entries

#get the summary of dataframe
print("information of dataframe", df.info())
print("description", df.describe())
print("gives no. of row and column", df.shape)
print("columns are present in dataframe:\n",df.columns)
print(df['First Name'])

# filtered data (print some data of a person who is male:)
filtered_data = df[df['Sex']=='Male']
print( "job title of only males: \n", filtered_data)

#aggregation with group by on csv file
group_data = df.groupby('Sex')['Index'].mean()
print("mean of indexes of male and female", group_data)

# data cleaning.......
new_df = df.dropna()
print(new_df.to_string())                   # print data after delete second row

#count unique values in a column
print(df['First Name'].value_counts())
