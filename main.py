import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'password'
database = 'dota_2'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE OR REPLACE VIEW frequency_of_character_selection AS 
SELECT characters.name AS name, COUNT(*) AS occurences
FROM game_session_character
         INNER JOIN characters on characters.id = game_session_character.character_id
GROUP BY name
ORDER BY occurences DESC;

SELECT * FROM frequency_of_character_selection;
'''
query_2 = '''
CREATE OR REPLACE VIEW number_of_characters_for_attributes AS
SELECT attributes.name, COUNT(*)
FROM characters
         INNER JOIN attributes on attributes.id = characters.main_attribute
GROUP BY attributes.name;

SELECT * FROM number_of_characters_for_attributes;
'''

query_3 = '''
CREATE OR REPLACE VIEW frequency_of_character_selection_of_certain_attribute AS
SELECT attributes.name AS attribute, COUNT(*) as occurences
FROM game_session_character
         INNER JOIN characters on characters.id = game_session_character.character_id
         INNER JOIN attributes on attributes.id = characters.main_attribute
GROUP BY attributes.name
ORDER BY occurences DESC;

SELECT * FROM frequency_of_character_selection_of_certain_attribute;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    characters = []
    characters_count = []

    for row in cur:
        characters.append(str(row[0]))
        characters_count.append(row[1])

    cur.execute(query_2)
    attributes = []
    attributes_count = []

    for row in cur:
        attributes.append(row[0] + '. ' + str(row[1]))
        attributes_count.append(row[1])

    cur.execute(query_3)
    attributes2 = []
    attributes_count2 = []

    for row in cur:
        attributes2.append(row[0])
        attributes_count2.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    fig.set_size_inches(15, 10)

    # bar
    bar_ax.set_title('Частота выбора персонажа в играх')
    bar_ax.set_xlabel('Персонаж')
    bar_ax.set_ylabel('Количество выборов')
    bar = bar_ax.bar(characters, characters_count)
    bar_ax.set_xticks(range(len(characters)))
    bar_ax.set_xticklabels(characters, rotation=30)

    # pie
    pie_ax.pie(attributes_count, labels=attributes, autopct='%1.1f%%')
    pie_ax.set_title('Количество персонажей конкретного аттрибута')

    # graph
    graph_ax.plot(attributes2, attributes_count2, marker='o')
    graph_ax.set_xlabel('Аттрибут')
    graph_ax.set_ylabel('Количество взятий')
    graph_ax.set_title('График зависимости частоты выбора персонажа от аттрибута')
    for gnr, count in zip(attributes2, attributes_count2):
        graph_ax.annotate(count, xy=(gnr, count), xytext=(7, 2), textcoords='offset points')

plt.get_current_fig_manager().resize(1400, 600)
plt.show()
