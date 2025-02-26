from fastapi import FastAPI
import pyodbc

app = FastAPI()

# Connexion à Azure SQL Database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=sqlsvr-db-trends.database.windows.net;'
    'DATABASE=trends;'
    'UID=datatrends;'
    'PWD=Tølibout2847'
)

@app.get("/trends")
async def get_trends():
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, topic, volume FROM Trends")
        rows = cursor.fetchall()
        return [{"id": row[0], "topic": row[1], "volume": row[2]} for row in rows]

