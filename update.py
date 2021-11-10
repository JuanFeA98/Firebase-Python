# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

# Conectamos con nuestra base de datos
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Update DATA

# Actualizar con un registro conocido
# db.collection('persons').document('MaqJaMy4TJLl5fHsW6BJ').update(
#     {'secondnumber': 10}
#     )

# Utilizar algunas funciones de firestore para actualizar
# db.collection('persons').document('MaqJaMy4TJLl5fHsW6BJ').update(
#     {'secondnumber': firestore.Increment(10)}
#     )

# Eliminar un elemento de un documento
db.collection('persons').document('MaqJaMy4TJLl5fHsW6BJ').update(
    {'books': firestore.ArrayRemove(['Book 1'])}
    )

# Agregar un elemento a un documento
db.collection('persons').document('MaqJaMy4TJLl5fHsW6BJ').update(
    {'books': firestore.ArrayUnion(['Book 2'])}
    )
