def generate_m2m_query():
    print("Welcome to the M2M Relationship SQL Query Generator!")

    # Get input from the user
    table1 = input("Enter the name of the first table: ")
    table1_column = input(f"Enter the primary key column name of {table1}: ")

    table2 = input("Enter the name of the second table: ")
    table2_column = input(f"Enter the primary key column name of {table2}: ")

    # Ask the user whether to use the default junction table name or specify a custom one
    use_default_name = input("Would you like to use the default naming convention for the junction table? (yes/no): ").strip().lower()

    if use_default_name == "yes":
        junction_table = f"{table1}_{table2}_relation"
    else:
        junction_table = input("Enter the custom name for the junction table: ")

    # Generate the SQL query
    query = f"""
    CREATE TABLE {junction_table} (
        {table1_column} INT,
        {table2_column} INT,
        PRIMARY KEY ({table1_column}, {table2_column}),
        FOREIGN KEY ({table1_column}) REFERENCES {table1}({table1_column}),
        FOREIGN KEY ({table2_column}) REFERENCES {table2}({table2_column})
    );
    """

    # Output the SQL query to a file named yourquery.sql
    with open("yourquery.sql", "w") as file:
        file.write(query)

    print("\nGenerated SQL query has been saved to yourquery.sql")

if __name__ == "__main__":
    generate_m2m_query()
