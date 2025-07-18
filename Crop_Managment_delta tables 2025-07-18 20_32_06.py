# Databricks notebook source
# 2. read the crop csv file(prints the data to understand the content) :
df_crop = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/dimension_volume/Dim_Crop.csv", header=True, inferSchema=True)
display(df_crop)

# COMMAND ----------

# delta table of dim_crop table
df_crop.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Dim_Crop_delta")

# COMMAND ----------

# 2. read the district csv file(prints the data to understand the content) :
df_district = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/dimension_volume/Dim_District.csv", header=True, inferSchema=True)
display(df_district)

# COMMAND ----------

# delta table of dim_district table
df_district.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Dim_District_delta")

# COMMAND ----------

# 2. read the season csv file(prints the data to understand the content) :
df_season = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/dimension_volume/Dim_Season.csv", header=True, inferSchema=True)
display(df_season)

# COMMAND ----------

# delta table of dim_season table
df_season.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Dim_Season_delta")

# COMMAND ----------

# 2. read the state csv file(prints the data to understand the content) :
df_state = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/dimension_volume/Dim_State.csv", header=True, inferSchema=True)
display(df_state)

# COMMAND ----------

# delta table of dim_state table
df_state.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Dim_State_delta")

# COMMAND ----------

# 2. read the year csv file(prints the data to understand the content) :
df_year = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/dimension_volume/Dim_Year.csv", header=True, inferSchema=True)
display(df_year)

# COMMAND ----------

# delta table of dim_year table
df_year.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Dim_Year_delta")

# COMMAND ----------

# 2. read the fact_crop_production csv file(prints the data to understand the content) :
df_production = spark.read.csv("dbfs:/Volumes/workspace/crop_managment_system/fact_volume/Fact_crop_production_sales.csv", header=True, inferSchema=True)
display(df_production)

# COMMAND ----------

# delta table of fact_crop_production table
df_production.write.format("delta").mode("overwrite").saveAsTable("workspace.crop_managment_system.Fact_crop_production_sales_delta")