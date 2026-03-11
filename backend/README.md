# Backend - API de Plateforme de Formation

## Vue d'ensemble
API FastAPI pour la gestion d'une plateforme de formation. Cette API permet de gérer les formations, les sessions, les utilisateurs, les inscriptions, les modules, les recommandations et les évaluations.

## Configuration

### Prérequis
- Python 3.8+
- SQLAlchemy
- FastAPI
- Uvicorn
- Python-jose
- LDAP3
- python-dotenv

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Variables d'environnement
Créer un fichier `.env` à la racine du backend avec les variables suivantes :

```
TOKEN_EXPIRE_MINUTES=30
LDAP_SERVER=your_ldap_server_address:389
DOCKER_APP_TK_EX_MIN=30
DOCKER_APP_LDAP_SERVER=your_ldap_server_address:389
```

### Démarrage du serveur
ou avec uvicorn :
```bash
uvicorn main:app --reload
```

L'API sera disponible à l'adresse : `http://localhost:8000`

---

## Endpoints

---

## Authentification

### 2. Login
#### `POST /login`
**Description** : Authentification via LDAP  
**Authentification** : Non requise  
**Corps de la requête** :
```json
{
  "email": "user@example.com",
  "password": "password"
}
```
**Réponse** :
```json
{
  "message": "Login successful"
}
```
Un cookie `access_token` est défini automatiquement.

### 3. Logout
#### `GET /logout`
**Description** : Déconnexion (supprime le cookie d'authentification)  
**Authentification** : Non requise  
**Réponse** :
```json
{
  "message": "Logout successful"
}
```

---

## Formations


### 5. Lister toutes les formations
#### `GET /formations/all`
**Description** : Récupère toutes les formations avec leurs détails  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "formations": [
    {
      "idFormation": 1,
      "nomFormation": "Formation 1",
      "descriptionFormation": "Description..."
    }
  ]
}
```

### 6. Créer une formation
#### `POST /formations/new`
**Description** : Crée une nouvelle formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `nomFormation` (string) : Nom de la formation
- `descriptionFormation` (string) : Description de la formation

**Exemple** :
```
POST /formations/new?nomFormation=Python%20Avancé&descriptionFormation=Formation%20avancée%20Python
```

**Réponse** :
```json
{
  "message": "Formation créée avec succès"
}
```

### 7. Modifier une formation
#### `PATCH /formations/patch`
**Description** : Met à jour une formation existante  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idFormation` (integer) : ID de la formation
- `nomFormation` (string) : Nouveau nom
- `descriptionFormation` (string) : Nouvelle description

**Exemple** :
```
PATCH /formations/patch?idFormation=1&nomFormation=Python%20Expert&descriptionFormation=Nouvelle%20description
```

**Réponse** :
```json
{
  "message": "Formation mise à jour avec succès"
}
```

### 8. Supprimer une formation
#### `DELETE /formations/delete`
**Description** : Supprime une formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idFormation` (integer) : ID de la formation

**Réponse** :
```json
{
  "message": "Formation supprimée avec succès"
}
```

---

## Sessions de Formation

### 9. Lister les sessions de formation
#### `GET /SessionDeFormation/all`
**Description** : Récupère toutes les sessions de formation  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "sessionsDeformations": [
    {
      "idSession": 1,
      "idFormation": 1,
      "dateDeDebut": "2024-01-15",
      "dateDeFin": "2024-03-15"
    }
  ]
}
```

### 10. Créer une session de formation
#### `POST /SessionDeFormation/new`
**Description** : Crée une nouvelle session de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idFormation` (integer) : ID de la formation
- `dateDeDebut` (string) : Date de début (format YYYY-MM-DD)
- `dateDeFin` (string) : Date de fin (format YYYY-MM-DD)

**Réponse** :
```json
{
  "message": "Session de formation créée avec succès"
}
```

### 11. Modifier une session de formation
#### `PATCH /SessionDeFormation/patch`
**Description** : Met à jour une session de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idSession` (integer) : ID de la session
- `idFormation` (integer) : Nouvel ID de formation
- `dateDeDebut` (string) : Nouvelle date de début
- `dateDeFin` (string) : Nouvelle date de fin

**Réponse** :
```json
{
  "message": "Session de formation mise à jour avec succès"
}
```

### 12. Supprimer une session de formation
#### `DELETE /SessionDeFormation/delete`
**Description** : Supprime une session de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idSession` (integer) : ID de la session

**Réponse** :
```json
{
  "message": "Session de formation supprimée avec succès"
}
```

---

## Utilisateurs

### 13. Lister les utilisateurs
#### `GET /Utilisateur/all`
**Description** : Récupère tous les utilisateurs  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "utilisateurs": [
    {
      "idUtilisateur": 1,
      "nomUtilisateur": "Dupont",
      "prenomUtilisateur": "Jean",
      "INEUtilisateur": "12345678",
      "dateDeNaissance": "1990-05-15",
      "idSession": 1
    }
  ]
}
```

### 14. Créer un utilisateur
#### `POST /Utilisateur/new`
**Description** : Crée un nouvel utilisateur  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `nomUtilisateur` (string) : Nom de famille
- `prenomUtilisateur` (string) : Prénom
- `INEUtilisateur` (string) : Numéro INE (Identifiant National Étudiant)
- `dateDeNaissance` (string) : Date de naissance (format YYYY-MM-DD)
- `idSession` (integer) : ID de la session

**Réponse** :
```json
{
  "message": "Utilisateur créé avec succès"
}
```

### 15. Modifier un utilisateur
#### `PATCH /Utilisateur/patch`
**Description** : Met à jour un utilisateur  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `nomUtilisateur` (string) : Nouveau nom
- `prenomUtilisateur` (string) : Nouveau prénom
- `INEUtilisateur` (string) : Nouvel INE
- `dateDeNaissance` (string) : Nouvelle date de naissance
- `idSession` (integer) : Nouvel ID session

**Réponse** :
```json
{
  "message": "Utilisateur mis à jour avec succès"
}
```

### 16. Supprimer un utilisateur
#### `DELETE /Utilisateur/delete`
**Description** : Supprime un utilisateur  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur

**Réponse** :
```json
{
  "message": "Utilisateur supprimé avec succès"
}
```

---

## Recommandations (IA)

### 17. Lister les recommandations
#### `GET /RecommandationsGenereesparLIA/all`
**Description** : Récupère toutes les recommandations générées par l'IA  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "recommandations": [
    {
      "idUtilisateur": 1,
      "idFormation": 2,
      "dateHeureRecommandation": "2024-01-15T10:30:00"
    }
  ]
}
```

### 18. Créer une recommandation
#### `POST /RecommandationsGenereesparLIA/new`
**Description** : Crée une nouvelle recommandation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `idFormation` (integer) : ID de la formation recommandée

**Note** : La date/heure est définie automatiquement au moment de la création

**Réponse** :
```json
{
  "message": "Recommandation créée avec succès"
}
```

### 19. Supprimer une recommandation
#### `DELETE /RecommandationsGenereesparLIA/delete`
**Description** : Supprime une recommandation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `idFormation` (integer) : ID de la formation

**Réponse** :
```json
{
  "message": "Recommandation supprimée avec succès"
}
```

---

## Inscriptions

### 20. Lister les inscriptions
#### `GET /Inscription/all`
**Description** : Récupère toutes les inscriptions  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "inscriptions": [
    {
      "idUtilisateur": 1,
      "idFormation": 1,
      "dateDInscription": "2024-01-10"
    }
  ]
}
```

### 21. Créer une inscription
#### `POST /Inscription/new`
**Description** : Crée une nouvelle inscription  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `idFormation` (integer) : ID de la formation
- `dateDInscription` (string) : Date d'inscription (format YYYY-MM-DD)

**Réponse** :
```json
{
  "message": "Inscription créée avec succès"
}
```

### 22. Supprimer une inscription
#### `DELETE /Inscription/delete`
**Description** : Supprime une inscription  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `idFormation` (integer) : ID de la formation

**Réponse** :
```json
{
  "message": "Inscription supprimée avec succès"
}
```

---

## Modules de Formation

### 23. Lister les modules de formation
#### `GET /ModulesDeFormation/all`
**Description** : Récupère tous les modules de formation  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "modulesDeFormation": [
    {
      "idModuleDeFormation": 1,
      "nomModule": "Module 1",
      "descriptionModule": "Description du module"
    }
  ]
}
```

### 24. Créer un module de formation
#### `POST /ModulesDeFormation/new`
**Description** : Crée un nouveau module de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `nomModule` (string) : Nom du module
- `descriptionModule` (string) : Description du module

**Réponse** :
```json
{
  "message": "Module de formation créé avec succès"
}
```

### 25. Modifier un module de formation
#### `PATCH /ModulesDeFormation/patch`
**Description** : Met à jour un module de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idModuleDeFormation` (integer) : ID du module
- `nomModule` (string) : Nouveau nom
- `descriptionModule` (string) : Nouvelle description

**Réponse** :
```json
{
  "message": "Module de formation mis à jour avec succès"
}
```

### 26. Supprimer un module de formation
#### `DELETE /ModulesDeFormation/delete`
**Description** : Supprime un module de formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idModuleDeFormation` (integer) : ID du module

**Réponse** :
```json
{
  "message": "Module de formation supprimé avec succès"
}
```

---

## Associations Formation-Module

### 27. Lister les associations formation-module
#### `GET /ComposerLaFormationDeModule/all`
**Description** : Récupère toutes les associations entre formations et modules  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "composerLaFormationDeModule": [
    {
      "idFormation": 1,
      "idModuleDeFormation": 1
    }
  ]
}
```

### 28. Créer une association formation-module
#### `POST /ComposerLaFormationDeModule/new`
**Description** : Associe un module à une formation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idFormation` (integer) : ID de la formation
- `idModuleDeFormation` (integer) : ID du module

**Réponse** :
```json
{
  "message": "Association entre formation et module créée avec succès"
}
```

### 29. Supprimer une association formation-module
#### `DELETE /ComposerLaFormationDeModule/delete`
**Description** : Supprime une association entre une formation et un module  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idFormation` (integer) : ID de la formation
- `idModuleDeFormation` (integer) : ID du module

**Réponse** :
```json
{
  "message": "Association entre formation et module supprimée avec succès"
}
```

---

## Évaluations

### 30. Lister les évaluations
#### `GET /Evaluations/all`
**Description** : Récupère toutes les évaluations  
**Authentification** : Requise ✅  
**Réponse** :
```json
{
  "evaluations": [
    {
      "idEvaluation": 1,
      "idUtilisateur": 1,
      "idModuleDeFormation": 1,
      "nomDeLEvaluation": "Évaluation 1",
      "modaliteDeLEvaluation": "Écrit",
      "dateDeDebutDeLEvaluation": "2024-02-01",
      "dateDeFinDeLEvaluation": "2024-02-15",
      "resultatNote": "18/20",
      "resultatDate": "2024-02-20"
    }
  ]
}
```

### 31. Créer une évaluation
#### `POST /Evaluations/new`
**Description** : Crée une nouvelle évaluation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idUtilisateur` (integer) : ID de l'utilisateur
- `idModuleDeFormation` (integer) : ID du module
- `nomDeLEvaluation` (string) : Nom de l'évaluation
- `modaliteDeLEvaluation` (string) : Modalité (ex: "Écrit", "Oral", etc.)
- `dateDeDebutDeLEvaluation` (string) : Date de début (format YYYY-MM-DD)
- `dateDeFinDeLEvaluation` (string) : Date de fin (format YYYY-MM-DD)
- `resultatNote` (string) : Note obtenue
- `resultatDate` (string) : Date du résultat (format YYYY-MM-DD)

**Réponse** :
```json
{
  "message": "Évaluation créée avec succès"
}
```

### 32. Modifier une évaluation
#### `PATCH /Evaluations/patch`
**Description** : Met à jour une évaluation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idEvaluation` (integer) : ID de l'évaluation
- `nomDeLEvaluation` (string) : Nouveau nom
- `modaliteDeLEvaluation` (string) : Nouvelle modalité
- `dateDeDebutDeLEvaluation` (string) : Nouvelle date de début
- `dateDeFinDeLEvaluation` (string) : Nouvelle date de fin
- `resultatNote` (string) : Nouvelle note
- `resultatDate` (string) : nouvelle date de résultat

**Réponse** :
```json
{
  "message": "Évaluation mise à jour avec succès"
}
```

### 33. Modifier le résultat d'une évaluation
#### `PATCH /Evaluations/patch/resultat`
**Description** : Met à jour uniquement le résultat d'une évaluation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idEvaluation` (integer) : ID de l'évaluation
- `resultatNote` (string) : Nouvelle note
- `resultatDate` (string) : Nouvelle date de résultat

**Réponse** :
```json
{
  "message": "Résultat de l'évaluation mis à jour avec succès"
}
```

### 34. Supprimer une évaluation
#### `DELETE /Evaluations/delete`
**Description** : Supprime une évaluation  
**Authentification** : Requise ✅  
**Paramètres de requête** :
- `idEvaluation` (integer) : ID de l'évaluation

**Réponse** :
```json
{
  "message": "Évaluation supprimée avec succès"
}
```

---

## Authentification

### Généralités
- **Type d'authentification** : JWT (JSON Web Token) via cookies
- **Serveur LDAP** : Authentification via un serveur LDAP externe
- **Session** : Les utilisateurs doivent se connecter pour accéder à la plupart des endpoints
- **Token** : Stocké dans un cookie `access_token` (httpOnly)
- **Expiration** : Le token expire après la durée définie en variable d'environnement (défaut: 30 minutes)

### Points d'accès public
- `POST /login` : Connexion
- `GET /logout` : Déconnexion

### Points d'accès protégés
Tous les autres endpoints nécessitent une authentification valide.

---


## Documentation interactive

Une fois le serveur lancé, consultez :
- **Swagger UI** : http://localhost:8000/docs

---

## Notes importantes

1. **Sécurité** : Tous les mots de passe sont validés via LDAP
2. **Base de données** : SQLAlchemy ORM utilisé pour les opérations
3. **CORS** : Configuration commentée, à activer si nécessaire
4. **Variables d'environnement** : Essentielles pour la configuration LDAP
