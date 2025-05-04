import psycopg2

conn = psycopg2.connect(
    dbname="into_the_void",
    user="postgres",
    password="iMSup3rG4y!",
    host="localhost",
    port="5432"
)

with conn:
    with conn.cursor() as curs:
        with open("data/sql/into_the_void.sql", "r") as f:
            sql_script = f.read()
            curs.execute(sql_script)

print("Database schema created successfully.")
