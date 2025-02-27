import pandas as pd
import pyodbc
import os

# Définition du chemin des fichiers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
clean_data_path = os.path.join(BASE_DIR, "data", "education_career_success_clean.csv")

# Connexion Azure SQL
conn = pyodbc.connect(
    'DRIVER=/usr/local/lib/libmsodbcsql.17.dylib;'
    'SERVER=sqlsvr-db-trends.database.windows.net;'
    'DATABASE=trends;'
    'UID=datatrends;'
    'PWD=Tølibout2847'
)

# Charger les données nettoyées
df = pd.read_csv(clean_data_path)

# Insérer les données
cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO EducationCareer (age, gender, high_school_gpa, university_ranking, university_gpa,
                                     field_of_study, internships_completed, certifications,
                                     soft_skills_score, networking_score, job_offers,
                                     starting_salary, career_satisfaction, years_to_promotion,
                                     work_life_balance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        row["Age"], row["Gender"], row["High_School_GPA"], row["University_Ranking"],
        row["University_GPA"], row["Field_of_Study"], row["Internships_Completed"],
        row["Certifications"], row["Soft_Skills_Score"], row["Networking_Score"],
        row["Job_Offers"], row["Starting_Salary"], row["Career_Satisfaction"],
        row["Years_to_Promotion"], row["Work_Life_Balance"]
    )

# Valider et fermer la connexion
conn.commit()
cursor.close()
conn.close()

print("Données insérées avec succès dans Azure SQL !")
