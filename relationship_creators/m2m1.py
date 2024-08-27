import psycopg2

def create_join_table(conn, schema1, table1, schema2, table2):
    with conn.cursor() as cur:
        # Derive the join table name
        join_table_name = f"{table1}_{table2}_join"

        print(f"Creating join table {join_table_name} in schema 'relations'.")

        # SQL command to create the join table
        create_table_sql = f"""
            CREATE TABLE relations.{join_table_name} (
                {table1}_id INT REFERENCES {schema1}.{table1}(id) ON DELETE CASCADE,
                {table2}_id INT REFERENCES {schema2}.{table2}(id) ON DELETE CASCADE,
                PRIMARY KEY ({table1}_id, {table2}_id)
            );
        """

        try:
            cur.execute(create_table_sql)
            conn.commit()
            print(f"Join table {join_table_name} created successfully in the 'relations' schema.")
        except Exception as e:
            print(f"An error occurred while creating the join table: {e}")
            conn.rollback()

if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname=" ",
        user=" ",
        password=" ",
        host=" ",
        port=" "
    )

    try:
        while True:
            schema1 = input("Enter the schema name for the first table: ")
            table1 = input("Enter the table name for the first table: ")

            schema2 = input("Enter the schema name for the second table: ")
            table2 = input("Enter the table name for the second table: ")

            create_join_table(conn, schema1, table1, schema2, table2)

            # Ask the user if they want to create another join table
            create_another = input("Do you want to create another join table? (yes/no): ").strip().lower()
            if create_another != 'yes':
                break
    finally:
        conn.close()
