import csv
import psycopg2

username = 'postgres'
password = 'password'
database = 'dota_2'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database)
cursor = conn.cursor()

get_all_tables_query = '''
SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE'
'''

def export_csv():
    output_path = '{}_export.csv'
    cursor.execute(get_all_tables_query)
    tables = []
    for row in cursor:
        tables.append(str(row[0]))

    for table in tables:
        cursor.execute('SELECT * FROM ' + table)
        with open(output_path.format(table), 'w') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow([i[0] for i in cursor.description])  # write headers
            csv_writer.writerows(cursor)


export_csv()
