import sqlite3

db_connection = sqlite3.connect('database.db')



with open('schema.sql') as sql_schema_file:
    db_connection.executescript(sql_schema_file.read())


db_cursor=db_connection.cursor()



db_cursor.execute(
    "INSERT INTO posts (title, content) VALUES (?,?)",
    ('first post', 'content of first post')
)


db_cursor.execute(
    "INSERT INTO posts (title, content) VALUES (?,?)",
    ('second post', 'contect of second post')

)



db_connection.commit()
db_connection.close()






