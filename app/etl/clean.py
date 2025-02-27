import pandas as pd
import os

# Construire le bon chemin du fichier source et du fichier nettoyé
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(BASE_DIR, "data", "education_career_success.csv")
clean_data_path = os.path.join(BASE_DIR, "data", "education_career_success_clean.csv")

# Charger le dataset
df = pd.read_csv(raw_data_path)

# Sélection des colonnes pertinentes
selected_columns = [
    "Age", "Gender", "High_School_GPA", "University_Ranking", "University_GPA",
    "Field_of_Study", "Internships_Completed", "Certifications",
    "Soft_Skills_Score", "Networking_Score", "Job_Offers",
    "Starting_Salary", "Career_Satisfaction", "Years_to_Promotion",
    "Work_Life_Balance"
]
df = df[selected_columns]

# Supprimer les doublons
df = df.drop_duplicates()

# Sauvegarder le dataset nettoyé
df.to_csv(clean_data_path, index=False)

print(f"Données nettoyées et sauvegardées dans : {clean_data_path}")
