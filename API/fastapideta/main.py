# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

from fastapi import FastAPI

# Conectamos con nuestra base de datos
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

docs = db.collection('titanic').get()

# Inicializamos nuestra app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/pasajeros")
async def get_pasajeros():
    a = []
    for i in range(len(docs)):
        print(docs[i].id)
        a.append((docs[i].to_dict()))

    return a

@app.get("/pasajeros/{id}")
async def get_color(id):

    result = db.collection('titanic').where('PassengerId', '==', int(id)).get()
    result = list(result)[0].to_dict() 

    return result