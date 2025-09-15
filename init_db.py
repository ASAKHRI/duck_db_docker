from pathlib import Path
import duckdb

DB_PATH = Path("my_database.duckdb")
conn = duckdb.connect(str(DB_PATH))


CSV_DIR = Path("data")
PARQUET_DIR = Path("parquet_data")


if CSV_DIR.exists():
    for csv_file in CSV_DIR.glob("*.csv"):
        table_name = csv_file.stem
        print(f"📥 Import du CSV {csv_file.name} → table `{table_name}`")
        try:
            conn.execute(f"""
                CREATE OR REPLACE TABLE {table_name} AS 
                SELECT * FROM read_csv_auto('{csv_file}')
            """)
            print(f"✅ Table `{table_name}` créée avec succès.")
        except Exception as e:
            print(f"❌ Erreur sur {csv_file.name}: {e}")


if PARQUET_DIR.exists():
    try:
        conn.execute("""
            CREATE OR REPLACE TABLE parquet_table AS
            SELECT * FROM read_parquet('parquet_data/*.parquet')
        """)
        print("✅ Table parquet_table créée depuis les fichiers Parquet.")
    except Exception as e:
        print(f"❌ Erreur sur les fichiers Parquet: {e}")

print("✅ Base DuckDB initialisée avec succès.")

