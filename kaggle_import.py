import psycopg2

username = 'postgres'
password = 'password'
database = 'dota_2'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database)
cursor = conn.cursor()

tables = {
    "attributes(id, name)": "C:/Users/Kolya/PycharmProjects/db_lab3/imports/attributes.csv",
    "character_role(character_id, role_id)": "C:/Users/Kolya/PycharmProjects/db_lab3/imports/character_role.csv",
    "characters(id, name, intelligence, strength, agility, main_attribute)": "C:/Users/Kolya/PycharmProjects/db_lab3/imports/characters.csv"
}

import_table_from_csv_query = "COPY {} FROM '{}' DELIMITER ',' CSV HEADER;"

with conn:
    cur = conn.cursor()

    for table, import_file in tables.items():
        cur.execute(import_table_from_csv_query.format(table, import_file))
