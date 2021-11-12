# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

import pandas as pd

# Conectamos con nuestra base de datos
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Cargamos nuestro dataset
df = pd.read_csv('https://gist.githubusercontent.com/JuanFeA98/ce470cf42a2b4449a314adef81211bf5/raw/d014b5d9cd080d99af363c2e511e16a84fc92cf3/CSS_colors.csv')

# Imprimir la primera fila del dataset
for i in range(len(df)):
    print(i)
    data = dict(df.iloc[i])
    db.collection('colors2').document(f'color_{i}').set(data)

    # print(dict(df.iloc[i]))
