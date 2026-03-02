from sqlalchemy import select

from fastipaconfig import app
from database.database import Session , Formation
from fastapi import  Depends, HTTPException
from fastapi.responses import JSONResponse

from utils.jwtConfig import create_access_token, get_current_user, verify_access_token
from request.requestLogin import RequestLogin


from dotenv import dotenv_values


config = dotenv_values(".env")

TOKEN_EXPIRE_MINUTES = int(config["TOKEN_EXPIRE_MINUTES"])

@app.get("/")
async def root():
    return {"message": "Bienvenue sur la plateforme de formation!"}

@app.get("/getallformations")
async def get_all_formations():
    session = Session()
    formations = session.query(Formation).all()
    return {"formations": [f.nomFormation for f in formations]}

@app.get("/formations/all")
async def get_all_formations(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Formation)
    formations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"formations": [f for f in formations]}

@app.post("/login")
async def login(user_request: RequestLogin):
    #TODO: Mettre en place une veritable verification de mot de passe en attendant magic word : "magicword123"
    if user_request.password != "magicword123":
        raise HTTPException(status_code=401, detail="Invalid password")
    token = create_access_token(email=user_request.email)

    
    response = JSONResponse(content="Login successful")
    response.set_cookie(key="access_token", value=token, httponly=True , max_age=TOKEN_EXPIRE_MINUTES* 60000)
    return response

@app.post("/logout")
async def logout():
    response = JSONResponse(content="Logout successful")
    response.delete_cookie(key="access_token")
    return response