# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

# Conectamos con nuestra base de datos
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Delete DATA
