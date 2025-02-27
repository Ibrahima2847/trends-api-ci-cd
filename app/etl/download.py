import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Vérifier si le fichier est déjà là
if not os.path.exists("data/education_and_career_success.csv"):
    # Initialiser l’API Kaggle
    api = KaggleApi()
    api.authenticate()

    # Télécharger le dataset
    api.dataset_download_files("adilshamim8/education-and-career-success", path="data", unzip=True)

    print("✅ Dataset téléchargé avec succès !")
else:
    print("✅ Dataset déjà présent !")
