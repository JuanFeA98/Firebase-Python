# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

# Conectamos con nuestra base de datos
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Read DATA

# Traer un documento por su ID
'''result = db.collection('persons').document('Sandra31').get()
# result = db.collection('persons').document('Sandra31').collection('books').get()

if result:
    if type(result) == list:
        print([i.to_dict() for i in result])
    else:
        print(result.to_dict())
else:
    print('No hay información')
'''
# Traer todos los documentos
'''docs = db.collection('persons').get()

for doc in docs:
    print(doc.to_dict())
'''
# Hacer querys con números
'''docs = db.collection('persons').where('number', '>', 30).get()
for doc in docs:
    print(doc.to_dict())
'''
# Hacer querys con strings
docs = db.collection('persons').where('firstname', 'in', ['Sandra']).get()
for doc in docs:
    print(doc.to_dict())
