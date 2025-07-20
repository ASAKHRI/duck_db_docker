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

docker run -p 8501:8501 duckdb_streamlit


### Accéder à l’application :

Ouvrez votre navigateur à l’adresse :
http://localhost:8501

requetez la base de donnée comme bon vous semble
