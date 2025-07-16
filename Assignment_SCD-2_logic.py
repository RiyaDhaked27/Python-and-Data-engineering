# Databricks notebook source
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

from pyspark.sql.functions import lit, to_date, current_date
# Add new columns to the customer DataFrame
customer_df = customer_df.withColumn("start_date", current_date()) \
                         .withColumn("end_date", lit("2200-01-01").cast("date")) \
                         .withColumn("current_flag", lit("Y").cast("boolean"))

# Display the updated DataFrame
customer_df.printSchema()
display(customer_df)   # now 26

# COMMAND ----------

# customer_df.write.format("delta").option("mergeSchema", "true").mode("overwrite").saveAsTable("workspace.book_cust.customer_table")

# COMMAND ----------

hcurrent_df = spark.read.table("workspace.book_cust.customer_table")
display(hcurrent_df)   # now 25

# COMMAND ----------

# Perform the union of customer_df and current_df
union_df = hcurrent_df.union(customer_df)

# Display the resulting DataFrame
display(union_df)

# COMMAND ----------

from delta.tables import DeltaTable
from pyspark.sql.functions import col, lit

# Step 3: Mark existing records as historical (set end_date where customer_id matches)
hcurrent_df = DeltaTable.forName(spark, "hcurrent_df")
hcurrent_df.alias("target").merge(
   customer_df.alias("source"),
    "target.customer_id = source.customer_id AND target.current_flag = 'Y'"
).whenMatchedUpdate(set={
    "end_date": col("source.start_date"),
    "Current_Flag": lit("F")
}).execute()

# Step 4: Insert new records
hcurrent_df.alias("target").merge(
   customer_df.alias("source"),
    "target.customer_id = source.customer_id AND target.start_date = source.start_date"
).whenNotMatchedInsertAll().execute()

display(spark.sql("select * from hcurrent_df Order By customer_id,start_date"))