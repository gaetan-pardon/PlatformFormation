from fastipaconfig import app
from database.database import Session , Formation


@app.get("/")
async def root():
    return {"message": "Bienvenue sur la plateforme de formation!"}

@app.get("/getallformations")
async def get_all_formations():
    session = Session()
    formations = session.query(Formation).all()
    return {"formations": [f.nomFormation for f in formations]}