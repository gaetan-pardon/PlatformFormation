import os
import sys

from pathlib import Path

from sqlalchemy import DateTime, create_engine, Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import sessionmaker, declarative_base
#import pyodbc

"""
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "app.db"

engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=engine)
session = Session()
"""

SERVER = "localhost"
DATABASE = "PlateformFormation"

DATABASE_URL = f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Formation(Base):
    """
    Représente une formation proposée par la plateforme.
    
    Attributes:
        id (int): Identifiant unique de la formation
        title (str): Titre de la formation
        description (str): Description détaillée de la formation
    """
    __tablename__ = 'Formations'
    idFormation = Column(Integer, primary_key=True, autoincrement=True)
    nomFormation = Column(String, nullable=False)
    descriptionFormation = Column(String, nullable=True)

class SessionDeFormation(Base):
    """
    Représente une session de formation. Par exemple Promo 2024 pour la formation "Développement Web".
    
    Attributes:
        id (int): Identifiant unique de la session de formation
        formation_id (int): Identifiant de la formation associée
        start_date (datetime): Date de début de la session
        end_date (datetime): Date de fin de la session
    """
    __tablename__ = 'SessionDeFormation'
    idSession = Column(Integer, primary_key=True, autoincrement=True)
    idFormation = Column(Integer, ForeignKey('Formations.idFormation'), nullable=False)
    dateDeDebut = Column(DateTime, nullable=False)
    dateDeFin = Column(DateTime, nullable=False)

class Utilisateur(Base):
    """
    Représente un utilisateur de la plateforme.
    
    Attributes:
        id (int): Identifiant unique de l'utilisateur
        nom (str): Nom de l'utilisateur
        email (str): Adresse email de l'utilisateur
        mot_de_passe (str): Mot de passe hashé de l'utilisateur
    """
    __tablename__ = 'Utilisateurs'
    idUtilisateur = Column(Integer, primary_key=True, autoincrement=True)
    nomUtilisateur = Column(String, nullable=False)
    prenomUtilisateur = Column(String, nullable=False)
    INEUtilisateur = Column(String, nullable=False, unique=True)
    dateDeNaissance = Column(DateTime, nullable=False)
    idSession = Column(Integer, ForeignKey('SessionDeFormation.idSession'), nullable=True)

class RecommandationsGenereesparLIA(Base):
    """
    Représente les recommandations générées par l'IA pour un utilisateur donné.
    
    Attributes:
        id (int): Identifiant unique de la recommandation
        utilisateur_id (int): Identifiant de l'utilisateur associé
        recommandations (str): Recommandations générées au format JSON ou texte
        date_generation (datetime): Date et heure de la génération des recommandations
    """
    __tablename__ = 'RecommandationsgenereesparLIA'
    idRecommandationsGenereesParLIA = Column(Integer, primary_key=True, autoincrement=True)
    idUtilisateur = Column(Integer, ForeignKey('Utilisateurs.idUtilisateur'), nullable=False)
    idFormation = Column(Integer, ForeignKey('Formations.idFormation'), nullable=False)
    dateHeureRecommandation = Column(TIMESTAMP, nullable=False)

class Inscription(Base):
    """
    Représente l'inscription d'un utilisateur à une session de formation.
    
    Attributes:
        id (int): Identifiant unique de l'inscription
        utilisateur_id (int): Identifiant de l'utilisateur inscrit
        session_id (int): Identifiant de la session de formation à laquelle l'utilisateur est inscrit
        date_inscription (datetime): Date et heure de l'inscription
    """
    __tablename__ = 'Inscriptions'
    idUtilisateur = Column(Integer, ForeignKey('Utilisateurs.idUtilisateur'),primary_key=True , nullable=False)
    idFormation = Column(Integer, ForeignKey('Formations.idFormation'),primary_key=True , nullable=False)
    dateDInscription = Column(TIMESTAMP, nullable=False)

class ModulesDeFormation(Base):
    """
    Représente les modules d'une formation.
    
    Attributes:
        id (int): Identifiant unique du module
        formation_id (int): Identifiant de la formation associée
        nom_module (str): Nom du module
        description_module (str): Description détaillée du module
    """
    __tablename__ = 'ModulesDeFormation'
    idModuleDeFormation = Column(Integer, primary_key=True, autoincrement=True)
    #idFormation = Column(Integer, ForeignKey('formations.idFormation'), nullable=False)
    nomModule = Column(String, nullable=False)
    descriptionModule = Column(String, nullable=True)

class ComposerLaFormationDeModule (Base):
    """
    Représente la relation entre les formations et leurs modules.
    
    Attributes:
        id (int): Identifiant unique de la relation
        formation_id (int): Identifiant de la formation
        module_id (int): Identifiant du module associé à la formation
    """
    __tablename__ = 'ComposerLaFormationDeModule'
    idFormation = Column(Integer, ForeignKey('Formations.idFormation'),primary_key=True , nullable=False)
    idModuleDeFormation = Column(Integer, ForeignKey('ModulesDeFormation.idModuleDeFormation'),primary_key=True , nullable=False)

class Evaluations(Base):
    """
    Représente les évaluations des utilisateurs pour les formations.
    
    Attributes:
        idEvaluation (int): Identifiant unique de l'évaluation
        idUtilisateur (int): Identifiant de l'utilisateur qui a évalué
        idModule (int): Identifiant du module évalué
        nomDeLEvaluation (str): Nom de l'évaluation
        modaliteDeLEvaluation (str): Modalité de l'évaluation
        dateDeDebutDeLEvaluation (datetime): Date et heure de l'évaluation
        dateDeFinDeLEvaluation (datetime): Date et heure de la fin de l'évaluation
        resultatNote (str): Résultat de l'évaluation (par exemple "Réussi", "Échoué", ou une note numérique)
        resultatDate (datetime): Date à laquelle le résultat de l'évaluation a été enregistré
    """
    __tablename__ = 'Evaluations'
    idEvaluation = Column(Integer, primary_key=True, autoincrement=True)
    idUtilisateur = Column(Integer, ForeignKey('Utilisateurs.idUtilisateur'), nullable=False)
    idModuleDeFormation = Column(Integer, ForeignKey('ModulesDeFormation.idModuleDeFormation'), nullable=False)
    nomDeLEvaluation = Column(String, nullable=False)
    modaliteDeLEvaluation = Column(String, nullable=False)
    dateDeDebutDeLEvaluation = Column(TIMESTAMP, nullable=False)
    dateDeFinDeLEvaluation = Column(TIMESTAMP, nullable=False)
    resultatNote = Column(String, nullable=True)
    resultatDate = Column(TIMESTAMP, nullable=True)


#Base.metadata.create_all(engine)