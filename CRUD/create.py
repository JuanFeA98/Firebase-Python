# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

# Conectamos con nuestra base de datos
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Data
nombre = str(input('Ingrese su nombre:'))
apellido = str(input('Ingrese su apellido:'))
numero = int(input('Ingrese su numero:'))
email = str(input('Ingrese su email:'))
username = str(input('Ingrese su username:'))

data = {
    'firstname': nombre,
    'lastname': apellido,
    'number': numero,
    'email': email,
    'username': username
}

# Create DATA

# Agregamos un documento a nuestra colleción
db.collection('persons').add(data)

# Establecer el ID del documento
db.collection('persons').document(username).set(data)

# Agregar un campo adicional
db.collection('persons').document(username).set({'address':'Bogotá'}, merge=True)

# Crear una subcolección
db.collection('persons').document(username).collection('books').add({'title':'Caballo de Troya'})

