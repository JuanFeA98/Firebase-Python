# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

# Conectamos con nuestra base de datos
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Delete DATA

# Borrar un documento
# db.collection("persons").document("PcN6WkNbxrmHevrsr5bI").delete()

# Borrar un campo
db.collection("persons").document("PcN6WkNbxrmHevrsr5bI").update({
    "number":firestore.DELETE_FIELD
    }
) 

