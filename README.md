# Projet Streamlit + DuckDB
## Description

Cette application Streamlit permet de requêter une base de données DuckDB localement.
La base de données est préchargée et l’application est contenue dans un conteneur Docker pour faciliter le déploiement.

## Prérequis

Docker installé sur votre machine

Une connexion Internet pour récupérer l’image Python lors de la première build

## Installation & lancement
### Cloner le repo git : 

ouvrir un terminal et clonez le repo :

git clone https://github.com/ASAKHRI/duck_db_docker.git

### accedez au dossier contenant le projet :

cd duck_db_docker

### construire l'image docker :

docker build -t duckdb_streamlit .

### Lancer le conteneur Docker :

docker run -p 8501:8501 -v %cd%\data:/app/data duckdb_streamlit


### Accéder à l’application :

Ouvrez votre navigateur à l’adresse :
http://localhost:8501

requetez la base de donnée comme bon vous semble
Mini Data Lake Local avec DuckDB + Streamlit
Description

Ce projet consiste à simuler un data lake local en utilisant DuckDB pour le stockage et la manipulation des données, et Streamlit pour créer une interface utilisateur interactive. Il permet de gérer facilement des datasets CSV/Parquet partitionnés et d’interagir avec eux de manière dynamique.

Objectifs

Simuler un data lake local.

Lire et manipuler des fichiers CSV/Parquet partitionnés avec DuckDB.

Créer une interface Streamlit pour gérer les tables et visualiser les données.

Dockeriser l’application pour faciliter le déploiement.

Fonctionnalités

Génération de datasets CSV avec colonnes de partition (année, mois, etc.).

Sauvegarde des données en fichiers Parquet partitionnés.

Lecture dynamique des fichiers Parquet avec DuckDB.

Application Streamlit permettant de :

Visualiser les tables DuckDB disponibles.

Supprimer une table existante.

Uploader un CSV et créer une nouvelle table.

Afficher les 5 premières lignes de chaque table.

Exporter une table en Parquet.

Appliquer des filtres dynamiques sur les données.

Afficher des graphiques interactifs à partir des tables.

Conteneurisation avec Docker pour un déploiement facile.

Technologies utilisées

Python

DuckDB

Streamlit

Pandas

Docker

Installation et utilisation
Pré-requis

Python 3.8+


Structure du projet
mini-data-lake/
├─ data/                  # Datasets CSV et Parquet
├─ app.py                 # Application Streamlit
├─ Dockerfile             # Dockerfile pour conteneurisation
├─ requirements.txt       # Dépendances Python
└─ README.md