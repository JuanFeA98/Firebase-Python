# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

from fastapi import FastAPI

# Conectamos con nuestra base de datos
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

docs = db.collection('colors2').get()
# print(len(docs))
# print(docs[1].to_dict())
a = []
for i in range(len(docs)):
    a.append(docs[i].to_dict())


# Inicializamos nuestra app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/colores")
async def get_colores():
    return a

@app.get("/colores/{id}")
async def get_color(id):
    result = db.collection('colors2').document(id).get()

    return result.to_dict()