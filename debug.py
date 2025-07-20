import duckdb

conn = duckdb.connect("my_database.duckdb")
tables = conn.execute("SHOW TABLES").fetchall()
print("Tables trouvées :", tables)
