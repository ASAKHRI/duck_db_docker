
import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path

DB_PATH = Path("my_database.duckdb")
conn = duckdb.connect(str(DB_PATH))

st.title("📊 Mini Data Lake Local avec DuckDB + Streamlit")


st.subheader("📂 Tables disponibles")
tables = conn.execute("SHOW TABLES").fetchdf()
st.dataframe(tables)


if not tables.empty:
    table_choice = st.selectbox("Choisir une table :", tables["name"].tolist())
    if st.button("Afficher 5 lignes"):
        preview = conn.execute(f"SELECT * FROM {table_choice} LIMIT 5").fetchdf()
        st.dataframe(preview)

    if st.button("Supprimer la table"):
        conn.execute(f"DROP TABLE IF EXISTS {table_choice}")
        st.success(f"✅ Table {table_choice} supprimée.")

    EXPORT_DIR = Path("data/output")
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    if st.button("Exporter en Parquet (partitionné par VendorID)"):
        df = conn.execute(f"SELECT * FROM {table_choice}").fetchdf()
        if "VendorID" not in df.columns:
            st.error("❌ Impossible : la colonne 'VendorID' n'existe pas dans cette table.")
        else:
            for vendor_id, group in df.groupby("VendorID"):
                out_path = EXPORT_DIR / f"{table_choice}_vendor{vendor_id}.parquet"
                group.to_parquet(out_path, index=False)
            st.success(f"✅ Export terminé → fichiers disponibles dans {EXPORT_DIR}")

st.subheader("⬆️ Uploader un CSV")
uploaded_file = st.file_uploader("Choisir un fichier CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    table_name = uploaded_file.name.replace(".csv", "")
    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
    st.success(f"✅ Table {table_name} créée avec succès.")


st.subheader("💬 Écrire une requête SQL")
default_query = ""
if not tables.empty:
    default_query = f"SELECT * FROM {tables['name'].iloc[0]} LIMIT 10"
query = st.text_area("Ta requête :", default_query)

if st.button("Exécuter la requête"):
    try:
        result = conn.execute(query).fetchdf()
        st.success("✅ Résultat :")
        st.dataframe(result)
    except Exception as e:
        st.error(f"❌ Erreur : {e}")
