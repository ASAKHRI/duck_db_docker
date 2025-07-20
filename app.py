import streamlit as st
import duckdb
from pathlib import Path

# Connexion en lecture à la base DuckDB à la racine
DB_PATH = Path("my_database.duckdb")
conn = duckdb.connect(str(DB_PATH), read_only=True)

st.title("🔎 Requête SQL sur la base DuckDB")

# Affiche les tables disponibles
st.subheader("📂 Tables disponibles")
tables = conn.execute("SHOW TABLES").fetchdf()
st.dataframe(tables)

# Zone de requête
st.subheader("💬 Requête SQL")
query = st.text_area("Ta requête :", "SELECT * FROM my_table LIMIT 10")

if st.button("Exécuter"):
    try:
        result = conn.execute(query).fetchdf()
        st.success("✅ Résultat :")
        st.dataframe(result)
    except Exception as e:
        st.error(f"❌ Erreur : {e}")
