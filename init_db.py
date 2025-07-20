from pathlib import Path
import duckdb

# Chemin de la base à la racine
DB_PATH = Path("my_database.duckdb")

# Connexion à la base (créée si inexistante)
conn = duckdb.connect(str(DB_PATH))

# Dossier des CSV
CSV_DIR = Path("data")
CSV_DIR.mkdir(exist_ok=True)

# Chargement de chaque CSV en table
csv_files = list(CSV_DIR.glob("*.csv"))
'''
for csv_file in csv_files:
    table_name = csv_file.stem
    print(f"Chargement de {csv_file.name} en tant que {table_name}")
    conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS 
        SELECT * FROM read_csv_auto('{csv_file}')
    """)
'''

for csv_file in csv_files:
    table_name = csv_file.stem
    print(f"📥 Tentative de chargement : {csv_file.name} → table `{table_name}`")
    try:
        conn.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS 
            SELECT * FROM read_csv_auto('{csv_file}')
        """)
        print(f"✅ Table `{table_name}` créée avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de l'import de `{csv_file.name}` : {e}")


print("✅ Base DuckDB initialisée avec succès.")
