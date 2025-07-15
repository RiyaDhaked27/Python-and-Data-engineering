# Databricks notebook source
dbutils.fs.ls("dbfs:/Volumes/workspace/book_cust/booking_volume/booking_25.csv")

# COMMAND ----------

# MAGIC %pip install pandas 
# MAGIC %restart_python

# COMMAND ----------

SPARK_VERSION = 3.2

# COMMAND ----------

#%pip install numpy==1.21
%pip install git+https://github.com/awslabs/python-deequ.git

# COMMAND ----------

import os
os.environ["SPARK_VERSION"] = "3.3"

# COMMAND ----------

from pyspark.sql.functions import col, lit, current_timestamp, sum as _sum
from delta.tables import DeltaTable
from pydeequ.checks import Check, CheckLevel
from pydeequ.verification import VerificationSuite, VerificationResult 

# COMMAND ----------

# define the input widget :
dbutils.widgets.text("arrival_date", "2025-07-25")
date_str = dbutils.widgets.get("arrival_date")

# COMMAND ----------

# df = spark.read.csv("dbfs:/Volumes/workspace/book_cust/booking_volume/booking_25.csv_{date_str}", header=True, inferSchema=True)
# display(df)

# read the file which take date dynamically as input:
booking_data = f"dbfs:/Volumes/workspace/book_cust/booking_volume/booking_{date_str}.csv"
print(booking_data)

customer_data = f"dbfs:/Volumes/workspace/book_cust/customer_volume/customer_{date_str}.csv"
print(customer_data)


# COMMAND ----------

# read booking data :
booking_df = spark.read.format("csv").option("header", True).option("inferSchema", True).option("quote", "\"").option("multiline", "True").load(booking_data)
booking_df.printSchema()
display(booking_df)

# read customer data :
customer_df = spark.read.format("csv").option("header", True).option("inferSchema", True).option("quote", "\"").option("multiline", "True").load(customer_data)
customer_df.printSchema()
display(customer_df)

# COMMAND ----------

# # data quality checks on booking data
# check_incremental = Check(spark, CheckLevel.Error, "Booking Data Check") \
#     .hasSize(lambda x: x > 0) \
#     .isUnique("booking_id", hint="Booking ID is not unique throught") \
#     .isComplete("customer_id") \
#     .isComplete("amount") \
#     .isNonNegative("amount") \
#     .isNonNegative("quantity") \
#     .isNonNegative("discount")

# COMMAND ----------

from pyspark.sql.functions import col

def isNull(df, column_name):
    return df.filter(col(column_name).isNull()).count() > 0

# Check if the DataFrame has any null values in the specified column
def check_isNull(df, column_name):
    if isNull(df, column_name):
        print(f"Column {column_name} contains null values.")
    
    else:
        print(f"Column {column_name} does not contain null values.")


    return df.filter(col(column_name).isNotNull())

a = check_isNull(booking_df, "customer_id")
c = check_isNull(a ,"booking_id")
b = check_isNull(c, "amount")
display(b)

# COMMAND ----------

# 5. Write the b dataframe to delta format :
# b.write.format("delta").mode("append").saveAsTable("workspace.book_cust.booking_table")

# COMMAND ----------

current_df = spark.read.table("workspace.book_cust.booking_table")
display(current_df) 

# COMMAND ----------

import pandas as pd
current_pd = current_df.toPandas()
new_pd = b.toPandas()          
merged_pd = pd.concat([current_pd, new_pd], ignore_index=True) #concat the two df and then drop the duplicates by keeping the last entry
merged_pd = merged_pd.drop_duplicates(subset=['booking_id'], keep='last')
print(f"Rows after merge: {len(merged_pd)}")
display(merged_pd)                 
merged_spark_df = spark.createDataFrame(merged_pd)
merged_spark_df.write.format("delta").mode("overwrite").saveAsTable("workspace.book_cust.booking_table")
updated_df = spark.read.table("workspace.book_cust.booking_table")
display(updated_df)