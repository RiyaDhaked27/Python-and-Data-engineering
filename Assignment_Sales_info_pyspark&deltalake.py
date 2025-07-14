# Databricks notebook source
# 1. using this path read the csv file into a dataframe :
dbutils.fs.ls("dbfs:/Volumes/workspace/default/skit_assignment/sales.csv")

# COMMAND ----------

# MAGIC %pip install pandas 
# MAGIC %restart_python

# COMMAND ----------

# 2. read the csv file(prints the data to understand the content) :
df = spark.read.csv("dbfs:/Volumes/workspace/default/skit_assignment/sales.csv", header=True, inferSchema=True)
display(df)     # inferSchema means - it will automatically infer the data type of each column

# COMMAND ----------

# 3. Apply the filter on sales transaction which has value more than 1000 :
df_filtered = df.filter((df.STATUS == 'Shipped') & (df.SALES > 1000))
display(df_filtered)


# COMMAND ----------

display(df_filtered.columns)

# COMMAND ----------

# 4. Select the columns EmployeeNumber, Age, Department, JobRole, MonthlyIncome, JobSatisfaction, Attrition from the dataframe:
df_selected = df_filtered.select('ORDERNUMBER', 'PRICEEACH', 'SALES', 'ORDERDATE', 'STATUS', 'YEAR_ID', 'MSRP', 'PRODUCTLINE', 'PRODUCTCODE', 'CUSTOMERNAME')
display(df_selected)

# COMMAND ----------

# 5. Write the dataframe to delta format :
df_selected.write.format("delta").mode("append").saveAsTable("workspace.default.agg_sales_data")

# COMMAND ----------


# # Read the delta format and display the data :
df_delta = spark.read.format("delta").table("workspace.default.agg_sales_data")
display(df_delta)

# COMMAND ----------

# Apply group by and aggregation function on sales column of the delta table:
df_grouped = df_delta.groupBy('YEAR_ID').agg({'SALES': 'sum'})
display(df_grouped)

# in sql
# %sql
# Select YEAR_ID, sum(SALES) as total_sales from workspace.default.agg_sales_data group by YEAR_ID

# COMMAND ----------

# 6. Version control(check the history of the dataframe):
df_history = spark.sql("DESCRIBE HISTORY workspace.default.agg_sales_data")
display(df_history)

# read the data from specific version of the delta table :
version_number = 1
df_specific_version = spark.read.format("delta").option("versionAsOf", version_number).table("workspace.default.agg_sales_data")
display(df_specific_version)

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume if not exists workspace.default.agg_transformed_data;

# COMMAND ----------

# 7. transformed dataframe :
df_transformed = df.filter((df.STATUS == 'Shipped') & (df.SALES > 1000)).select('ORDERNUMBER', 'PRICEEACH', 'SALES', 'ORDERDATE', 'STATUS', 'YEAR_ID', 'MSRP', 'PRODUCTLINE', 'PRODUCTCODE', 'CUSTOMERNAME')
display(df_transformed)

# write the transformed dataframe to a delta table with partitioning by YEAR_ID :
df_transformed.write.format("delta").mode("overwrite").partitionBy("YEAR_ID").save("/Volumes/workspace/default/agg_transformed_data/agg_sales_data")