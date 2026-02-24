from fastipaconfig import app

@app.get("/")
async def root():
    return {"message": "Bienvenue sur la plateforme de formation!"}