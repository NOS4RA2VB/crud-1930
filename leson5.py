import sqlite3

connection = sqlite3.connect('json.db')
cursor = connection.cursor()

# .execute() - выполняет один запрос
# .executesript() - выполняет множкство запросов

# cursor.executescript('''
# DROP TABLE IF EXISTS names;
# CREATE TABLE IF NOT EXISTS names(
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       name TEXT
# );
# ''')
# connection.commit() # выполнение запроса с бд
# connection.close()