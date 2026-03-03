from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# initialisation de l'application fastapi
app = FastAPI(title="api de gestion d'accessoires telephoniques")

# configuration cors pour permettre a angular de lire les donnees
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# definition du modele pour un accessoire
class accessoire(BaseModel):
    id: int
    nom: str
    marque: str
    prix: float
    disponible: bool

# notre base de donnees fictive
db_accessoires = [
    {"id": 1, "nom": "chargeur rapide 25w", "marque": "samsung", "prix": 29.99, "disponible": True},
    {"id": 2, "nom": "ecouteurs bluetooth", "marque": "apple", "prix": 150.0, "disponible": True},
    {"id": 3, "nom": "coque en silicone", "marque": "xiaomi", "prix": 15.5, "disponible": False},
    {"id": 4, "nom": "protection d'ecran", "marque": "huawei", "prix": 10.0, "disponible": True}
]

@app.get("/")
def message_bienvenue():
    return {"message": "bienvenue sur l'api de gestion des accessoires"}

# cette route est celle que angular va appeler
@app.get("/accessoires", response_model=List[accessoire])
def lire_tous_les_accessoires():
    return db_accessoires