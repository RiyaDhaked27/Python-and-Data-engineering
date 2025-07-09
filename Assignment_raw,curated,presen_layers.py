# Databricks notebook source
df = spark.sql("select * from skit.tables")
display(df)


# COMMAND ----------

# only Raw table :
df = spark.table("skit.tables")
display(df)

from collections import defaultdict
tables = defaultdict(list)
for row in df.collect():
    table_name = row['raw table name']
    column_name = row['raw table column']
    column_data_type = row['raw table datatype']

tables[table_name].append(f"{column_name} {column_data_type}")

for table_name, columns in tables.items():
    col_def = ", ".join(columns)
    drop_sql = f"DROP TABLE IF EXISTS {table_name}"
    spark.sql(drop_sql)
    create_sql = f"CREATE TABLE {table_name} ({col_def})"
    spark.sql(create_sql)
    print(f"Created Table: {table_name}")
                              

# COMMAND ----------

# only Curated table :
df = spark.table("skit.tables")
display(df)

from collections import defaultdict
tables = defaultdict(list)
for row in df.collect():
    table_name = row['curated table name']
    column_name = row['curated table column']
    column_data_type = row['curated table datatype']

tables[table_name].append(f"{column_name} {column_data_type}")

for table_name, columns in tables.items():
    col_def = ", ".join(columns)
    drop_sql = f"DROP TABLE IF EXISTS {table_name}"
    spark.sql(drop_sql)
    create_sql = f"CREATE TABLE {table_name} ({col_def})"
    spark.sql(create_sql)
    print(f"Created Table: {table_name}")



# only presentation table :
df = spark.table("skit.tables")
display(df)

from collections import defaultdict
tables = defaultdict(list)
for row in df.collect():
    table_name = row['presentation table name']
    column_name = row['presentation table column']
    column_data_type = row['presentation table datatype']

tables[table_name].append(f"{column_name} {column_data_type}")

for table_name, columns in tables.items():
    col_def = ", ".join(columns)
    drop_sql = f"DROP TABLE IF EXISTS {table_name}"
    spark.sql(drop_sql)
    create_sql = f"CREATE TABLE {table_name} ({col_def})"
    spark.sql(create_sql)
    print(f"Created Table: {table_name}")

# COMMAND ----------

# three tables - raw, curated, presentation using function :
def drop_and_create_tables(tables_dict):
    for table_name, columns in tables_dict.items():
        col_def = ", ".join(columns)
        drop_sql = f"DROP TABLE IF EXISTS {table_name}"
        create_sql = f"CREATE TABLE {table_name} ({col_def})"
        
        spark.sql(drop_sql)
        spark.sql(create_sql)
        print(f"Created Table: {table_name}")

df_metadata = spark.table("skit.tables")
display(df_metadata)

from collections import defaultdict
raw_tables = defaultdict(list)
curated_tables = defaultdict(list)
presentation_tables = defaultdict(list)

for row in df_metadata.collect():
    table_name = row['raw table name']
    col_def = f"{row['raw table column']} {row['raw table datatype']}"
    raw_tables[table_name].append(col_def)

    table_name = row['curated table name']
    col_def = f"{row['curated table column']} {row['curated table datatype']}"
    curated_tables[table_name].append(col_def)

    table_name = row['presentation table name']
    col_def = f"{row['presentation table column']} {row['presentation table datatype']}"
    presentation_tables[table_name].append(col_def)

# Create raw tables
drop_and_create_tables(raw_tables)

# Create curated tables
drop_and_create_tables(curated_tables)

# Create presentation tables
drop_and_create_tables(presentation_tables)