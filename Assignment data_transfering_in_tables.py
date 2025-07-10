# Databricks notebook source
df = spark.sql("select * from skit.info_metadata2")
display(df)

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

df_metadata = spark.table("skit.info_metadata2")
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

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into users values('1','John Doe');
# MAGIC insert into users values('2', 'jonny');
# MAGIC insert into users values('3', 'jinny');
# MAGIC     select *from default.users;

# COMMAND ----------

# MAGIC %sql
# MAGIC     select *from default.cur_user;

# COMMAND ----------

# MAGIC %sql
# MAGIC     select *from default.per_user;

# COMMAND ----------

# MAGIC %sql
# MAGIC select *from default.cur_user;

# COMMAND ----------

dbutils.widgets.text("process_name", " ")
dbutils.widgets.get("process_name")
input_process_names = [name.strip() for name in "process_name".split(',') if name.strip()]
filtered_df = df_metadata.filter(df_metadata['Process Name'].isin(input_process_names))
display(filtered_df)


# COMMAND ----------

raw_table_name = df_metadata.select("raw table name").distinct().collect()[0]["raw table name"]

users_df = spark.table(raw_table_name)
display(users_df)


for row in df_metadata.collect():
    logic = row['logic']
    if logic:
        filtered_df = users_df.filter(logic) 
        # display(filtered_df)
        
        if row['curated table name']:

            filtered_df.write.insertInto(row['curated table name'])
        
        if row['presentation table name']:
            filtered_df.write.insertInto(row['presentation table name'])


cur_user_df = spark.table("cur_user")
display(cur_user_df)

per_user_df = spark.table("per_user")
display(per_user_df)