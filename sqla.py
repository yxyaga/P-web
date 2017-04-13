import sqlite3
conn = sqlite3.connect("new.db")
connmem = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE population(city TEXT,state TEXT,population INT)""")
conn.close()
