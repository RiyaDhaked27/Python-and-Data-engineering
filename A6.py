# ************************************ Assignment 6 ***********************************************

import pandas as pd
# question 1 ********************
data = {'dates': pd.to_datetime(['2025-04-22','2025-06-21','2025-06-22','2025-02-20','2025-06-22']), 'col1': ['course1','course2','course3','course4','course5']}
df = pd.DataFrame(data)
#print(df)
ts = pd.Series(df['col1'].values, index=df['dates'],)
print(ts)

# question 2*********************
df1 = pd.DataFrame({"Name":['riya','bhumi','jai','lalit'], "id":[1,2,3,4]})           #create first dataframe
print("\n dataframe 1:",df1)
df2 = pd.DataFrame({"Score":[100,200,300,400], "id":[1,5,3,6]})                       #create second dataframe
print("\n dataframe 2:",df2)

#inner merge.......
res1 = pd.merge(df1,df2, on="id", how="inner")
print("\n inner merge is:", res1)

#left join.....
res2 = pd.merge(df1,df2, on="id", how="left")
print("\n left join is:", res2)
# missing values :
#  Notice how ID=2 and ID=4 has NaN for Score (no match in df2)

#right join.....
res3 = pd.merge(df1,df2, on="id", how="right")
print("\n right join is:", res3)
# missing values :
#  Notice how ID=5 and ID=6 has NaN for name (no match in df1)

#index based join..........
import pandas as pd

# Create two DataFrames with index
dfl = pd.DataFrame({'Name': ['Aniket', 'Bunny', 'Chetan']}, index=[1, 2, 3])
dfr = pd.DataFrame({'Score': [90, 85, 78]}, index=[2, 3, 4])

# Join on index
res = dfl.join(dfr, rsuffix='_right', lsuffix='_left')
print("Index-Based Join Result:", res)

# right or inner join by index based
res_inner = dfl.join(dfr, how='right')
print("Right Join Based on Index:", res_inner)

# Question 3 ******************************

# Create three DataFrames
dfA = pd.DataFrame({'ID': [1, 2], 'Name': ['riya', 'Jonny']})
dfB = pd.DataFrame({'ID': [3, 4], 'Name': ['bhumi', 'jai']})
dfC = pd.DataFrame({'ID': [2, 3, 4], 'Score': [95, 80, 88]})

# Concatenate dfA and dfB vertically
concat_df = pd.concat([dfA, dfB], ignore_index=True)
print("\n Concatenated dfA and dfB:\n", concat_df)

# Merge with dfC on 'ID'
merged = pd.merge(concat_df, dfC, on='ID', how='left')
print("\n Merged with dfC:\n", merged)


# difference between df.join and pd.merge:

# ..df.join Joins on the index by default and pd.merge Joins on common columns by default
#..df.join Index-to-index join and pd.merge Column-to-column join using like on="column name"
#..df.join limited keys support and pd.merge fully supports multiple keys (like, on=['A','B'])





