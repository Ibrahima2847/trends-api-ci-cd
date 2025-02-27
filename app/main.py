from fastapi import FastAPI
from app.routers import trends

app = FastAPI()

# Inclure les routes
app.include_router(trends.router)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API Education & Carrière "}
