from sqlalchemy import select

from fastipaconfig import app
from database.database import Session , Formation , SessionDeFormation , Utilisateur , RecommandationsGenereesparLIA , Inscription , ModulesDeFormation , ComposerLaFormationDeModule , Evaluations
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

@app.get("/SessionDeFormation/all")
async def get_all_session_de_formation(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(SessionDeFormation)
    sessionsDeformations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"sessionsDeformations": [f for f in sessionsDeformations]}


@app.get("/Utilisateur/all")
async def get_all_utilisateurs(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Utilisateur)
    utilisateurs = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"utilisateurs": [f for f in utilisateurs]}


@app.get("/RecommandationsGenereesparLIA/all")
async def get_all_recommandations(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(RecommandationsGenereesparLIA)
    recommandations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"recommandations": [f for f in recommandations]}


@app.get("/Inscription/all")
async def get_all_inscriptions(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Inscription)
    inscriptions = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"inscriptions": [f for f in inscriptions]}


@app.get("/ModulesDeFormation/all")
async def get_all_modules_de_formation(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(ModulesDeFormation)
    formations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"modulesDeFormation": [f for f in formations]}

@app.get("/ComposerLaFormationDeModule/all")
async def get_all_composer_la_formation_de_module(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(ComposerLaFormationDeModule)
    formations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"composerLaFormationDeModule": [f for f in formations]}

@app.get("/Evaluations/all")
async def get_all_evaluations(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Evaluations)
    evaluations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"evaluations": [f for f in evaluations]}

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