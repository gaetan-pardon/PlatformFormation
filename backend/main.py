from sqlalchemy import select

from fastipaconfig import app
from database.database import Session , Formation , SessionDeFormation , Utilisateur , RecommandationsGenereesparLIA , Inscription , ModulesDeFormation , ComposerLaFormationDeModule , Evaluations
from fastapi import  Depends, HTTPException
from fastapi.responses import JSONResponse

from utils.jwtConfig import create_access_token, get_current_user, verify_access_token
from request.requestLogin import RequestLogin
from datetime import datetime

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

@app.post("/formations/new")
async def create_new_formation(nomFormation: str , descriptionFormation: str , current_user : str = Depends(get_current_user)):
    session = Session()
    formation = Formation(nomFormation=nomFormation, descriptionFormation=descriptionFormation)
    session.add(formation)
    session.commit()
    return {"message": "Formation créée avec succès"}

@app.get("/SessionDeFormation/all")
async def get_all_session_de_formation(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(SessionDeFormation)
    sessionsDeformations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"sessionsDeformations": [f for f in sessionsDeformations]}

@app.post("/SessionDeFormation/new")
async def create_new_session_de_formation( idFormation: int , dateDeDebut: str , dateDeFin: str , current_user : str = Depends(get_current_user)):
    session = Session()
    sessionDeFormation = SessionDeFormation(idFormation=idFormation, dateDeDebut=dateDeDebut, dateDeFin=dateDeFin)
    session.add(sessionDeFormation)
    session.commit()
    return {"message": "Session de formation créée avec succès"}

@app.get("/Utilisateur/all")
async def get_all_utilisateurs(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Utilisateur)
    utilisateurs = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"utilisateurs": [f for f in utilisateurs]}

@app.post("/Utilisateur/new")
async def create_new_utilisateur(nomUtilisateur: str , prenomUtilisateur: str , INEUtilisateur: str , dateDeNaissance: str , idSession: int  , current_user : str = Depends(get_current_user)):
    session = Session()
    utilisateur = Utilisateur(nomUtilisateur=nomUtilisateur, prenomUtilisateur=prenomUtilisateur, INEUtilisateur=INEUtilisateur, dateDeNaissance=dateDeNaissance, idSession=idSession)
    session.add(utilisateur)
    session.commit()
    return {"message": "Utilisateur créé avec succès"}



@app.get("/RecommandationsGenereesparLIA/all")
async def get_all_recommandations(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(RecommandationsGenereesparLIA)
    recommandations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"recommandations": [f for f in recommandations]}

@app.post("/RecommandationsGenereesparLIA/new")
async def create_new_recommandation(idUtilisateur: int , idFormation: int , current_user : str = Depends(get_current_user)):
    session = Session()
    recommandation = RecommandationsGenereesparLIA(idUtilisateur=idUtilisateur, idFormation=idFormation, dateHeureRecommandation=datetime.now())
    session.add(recommandation)
    session.commit()
    return {"message": "Recommandation créée avec succès"}


@app.get("/Inscription/all")
async def get_all_inscriptions(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Inscription)
    inscriptions = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"inscriptions": [f for f in inscriptions]}

@app.post("/Inscription/new")
async def create_new_inscription(idUtilisateur: int , idFormation: int , dateDInscription: str , current_user : str = Depends(get_current_user)):
    session = Session()
    inscription = Inscription(idUtilisateur=idUtilisateur, idFormation=idFormation, dateDInscription=dateDInscription)
    session.add(inscription)
    session.commit()
    return {"message": "Inscription créée avec succès"}

@app.get("/ModulesDeFormation/all")
async def get_all_modules_de_formation(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(ModulesDeFormation)
    formations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"modulesDeFormation": [f for f in formations]}

@app.post("/ModulesDeFormation/new")
async def create_new_module_de_formation(nomModule: str , descriptionModule: str , current_user : str = Depends(get_current_user)):
    session = Session()
    moduleDeFormation = ModulesDeFormation(nomModule=nomModule, descriptionModule=descriptionModule)
    session.add(moduleDeFormation)
    session.commit()
    return {"message": "Module de formation créé avec succès"}

@app.patch("/ModulesDeFormation/patch")
async def update_module_de_formation(idModuleDeFormation: int , nomModule: str , descriptionModule: str , current_user : str = Depends(get_current_user)):
    session = Session()
    moduleDeFormation = session.query(ModulesDeFormation).filter(ModulesDeFormation.idModuleDeFormation == idModuleDeFormation).first()
    if moduleDeFormation is None:
        raise HTTPException(status_code=404, detail="Module de formation non trouvé")
    moduleDeFormation.nomModule = nomModule
    moduleDeFormation.descriptionModule = descriptionModule
    session.commit()
    return {"message": "Module de formation mis à jour avec succès"}

@app.delete("/ModulesDeFormation/delete")
async def delete_module_de_formation(idModuleDeFormation: int , current_user : str = Depends(get_current_user)):
    session = Session()
    moduleDeFormation = session.query(ModulesDeFormation).filter(ModulesDeFormation.idModuleDeFormation == idModuleDeFormation).first()
    if moduleDeFormation is None:
        raise HTTPException(status_code=404, detail="Module de formation non trouvé")
    session.delete(moduleDeFormation)
    session.commit()
    return {"message": "Module de formation supprimé avec succès"}

@app.get("/ComposerLaFormationDeModule/all")
async def get_all_composer_la_formation_de_module(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(ComposerLaFormationDeModule)
    formations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"composerLaFormationDeModule": [f for f in formations]}

@app.post("/ComposerLaFormationDeModule/new")
async def create_new_composer_la_formation_de_module(idFormation: int , idModuleDeFormation: int , current_user : str = Depends(get_current_user)):
    session = Session()
    composerLaFormationDeModule = ComposerLaFormationDeModule(idFormation=idFormation, idModuleDeFormation=idModuleDeFormation)
    session.add(composerLaFormationDeModule)
    session.commit()
    return {"message": "Association entre formation et module créée avec succès"}

@app.delete("/ComposerLaFormationDeModule/delete")
async def delete_composer_la_formation_de_module(idFormation: int , idModuleDeFormation: int , current_user : str = Depends(get_current_user)):
    session = Session()
    association = session.query(ComposerLaFormationDeModule).filter(ComposerLaFormationDeModule.idFormation == idFormation, ComposerLaFormationDeModule.idModuleDeFormation == idModuleDeFormation).first()
    if association is None:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    session.delete(association)
    session.commit()
    return {"message": "Association entre formation et module supprimée avec succès"}

@app.get("/Evaluations/all")
async def get_all_evaluations(current_user : str = Depends(get_current_user)):
    #print(f"Utilisateur connecté : {current_user}")
    session = Session()
    stmt= select(Evaluations)
    evaluations = session.scalars(stmt)
    #return {"formations": [f.nomFormation for f in formations]}
    return  {"evaluations": [f for f in evaluations]}

@app.post("/Evaluations/new")
async def create_new_evaluation(idUtilisateur: int , idModuleDeFormation: int ,nomDeLEvaluation: str ,modaliteDeLEvaluation: str , dateDeDebutDeLEvaluation: str , dateDeFinDeLEvaluation: str , resultatNote: str ,resultatDate: str , current_user : str = Depends(get_current_user)):
    session = Session()
    evaluation = Evaluations(idUtilisateur=idUtilisateur, idModuleDeFormation=idModuleDeFormation, nomDeLEvaluation=nomDeLEvaluation, modaliteDeLEvaluation=modaliteDeLEvaluation, dateDeDebutDeLEvaluation=dateDeDebutDeLEvaluation, dateDeFinDeLEvaluation=dateDeFinDeLEvaluation, resultatNote=resultatNote, resultatDate=resultatDate)
    session.add(evaluation)
    session.commit()
    return {"message": "Évaluation créée avec succès"}

@app.patch("/Evaluations/patch")
async def update_evaluation(idEvaluation: int , nomDeLEvaluation: str , modaliteDeLEvaluation: str , dateDeDebutDeLEvaluation: str , dateDeFinDeLEvaluation: str , resultatNote: str ,resultatDate: str , current_user : str = Depends(get_current_user)):
    session = Session()
    evaluation = session.query(Evaluations).filter(Evaluations.idEvaluation == idEvaluation).first()
    if evaluation is None:
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    evaluation.nomDeLEvaluation = nomDeLEvaluation
    evaluation.modaliteDeLEvaluation = modaliteDeLEvaluation
    evaluation.dateDeDebutDeLEvaluation = dateDeDebutDeLEvaluation
    evaluation.dateDeFinDeLEvaluation = dateDeFinDeLEvaluation
    evaluation.resultatNote = resultatNote
    evaluation.resultatDate = resultatDate
    session.commit()
    return {"message": "Évaluation mise à jour avec succès"}

@app.patch("/Evaluations/patch/resultat")
async def update_evaluation_resultat(idEvaluation: int , resultatNote: str ,resultatDate: str , current_user : str = Depends(get_current_user)):
    session = Session()
    evaluation = session.query(Evaluations).filter(Evaluations.idEvaluation == idEvaluation).first()
    if evaluation is None:
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    evaluation.resultatNote = resultatNote
    evaluation.resultatDate = resultatDate
    session.commit()
    return {"message": "Résultat de l'évaluation mis à jour avec succès"}

@app.delete("/Evaluations/delete")
async def delete_evaluation(idEvaluation: int , current_user : str = Depends(get_current_user)):
    session = Session()
    evaluation = session.query(Evaluations).filter(Evaluations.idEvaluation == idEvaluation).first()
    if evaluation is None:
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    session.delete(evaluation)
    session.commit()
    return {"message": "Évaluation supprimée avec succès"}

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