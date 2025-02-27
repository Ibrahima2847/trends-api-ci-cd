from fastapi import APIRouter, HTTPException
from app.database import get_db_connection

router = APIRouter()

@router.get("/trends")
async def get_trends():
    """ Récupère toutes les tendances de la base SQL """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EducationCareer")
    rows = cursor.fetchall()
    
    trends = []
    for row in rows:
        trends.append({
            "id": row[0], "age": row[1], "gender": row[2],
            "high_school_gpa": row[3], "university_ranking": row[4],
            "university_gpa": row[5], "field_of_study": row[6],
            "internships_completed": row[7], "certifications": row[8],
            "soft_skills_score": row[9], "networking_score": row[10],
            "job_offers": row[11], "starting_salary": row[12],
            "career_satisfaction": row[13], "years_to_promotion": row[14],
            "work_life_balance": row[15]
        })
    
    cursor.close()
    conn.close()
    return trends

@router.get("/trends/{id}")
async def get_trend(id: int):
    """ Récupère une seule tendance en fonction de l'ID """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EducationCareer WHERE id = ?", id)
    row = cursor.fetchone()
    
    if not row:
        raise HTTPException(status_code=404, detail="Tendance non trouvée")

    trend = {
        "id": row[0], "age": row[1], "gender": row[2],
        "high_school_gpa": row[3], "university_ranking": row[4],
        "university_gpa": row[5], "field_of_study": row[6],
        "internships_completed": row[7], "certifications": row[8],
        "soft_skills_score": row[9], "networking_score": row[10],
        "job_offers": row[11], "starting_salary": row[12],
        "career_satisfaction": row[13], "years_to_promotion": row[14],
        "work_life_balance": row[15]
    }

    cursor.close()
    conn.close()
    return trend
