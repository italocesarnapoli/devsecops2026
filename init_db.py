import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

senha_usuario = input("Senha do usuário: ")

cur.execute("INSERT INTO users (username, passwd) VALUES (?, ?)",
            ('admin', generate_password_hash(senha_usuario))
            )

connection.commit()
connection.close()