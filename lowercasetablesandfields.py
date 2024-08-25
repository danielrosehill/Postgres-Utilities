import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Query to get all table and column names
cur.execute("""
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema = 'public';
""")

# Iterate over all columns and generate the ALTER TABLE statements
for table_name, column_name in cur.fetchall():
    new_column_name = column_name.lower().replace(" ", "_")
    if column_name != new_column_name:
        sql = f'ALTER TABLE "{table_name}" RENAME COLUMN "{column_name}" TO "{new_column_name}";'
        print(sql)
        cur.execute(sql)

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()
