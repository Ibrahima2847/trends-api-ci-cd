import os

# Construire le bon chemin vers le dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Aller au dossier racine
print(BASE_DIR)
dataset_path = os.path.join(BASE_DIR, "data", "education_career_success.csv")
print(dataset_path)

# Vérifier si le fichier existe
if not os.path.exists(dataset_path):
    print(f"❌ Fichier introuvable : {dataset_path}")
    exit()

print(f"✅ Chargement du fichier : {dataset_path}")

import pandas as pd
df = pd.read_csv(dataset_path)

print(df.head())  

# Charger le dataset
df = pd.read_csv(dataset_path)

# Afficher les premières lignes
print("Aperçu des données :")
print(df.head())

# Afficher les informations générales (types, valeurs nulles)
print("\nInformations générales :")
print(df.info())

# Vérifier les valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# Vérifier les doublons
print("\nNombre de doublons :", df.duplicated().sum())

# Résumé statistique des colonnes numériques
print("\nStatistiques générales :")
print(df.describe())
