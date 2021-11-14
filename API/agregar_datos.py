# Importamos nuestras librerias
import firebase_admin
from firebase_admin import credentials, firestore

import pandas as pd
import numpy as np

# Conectamos con nuestra base de datos
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Creamos una referencia a nuestra base de datos
db = firestore.client()

# Cargamos nuestro dataset
# df = pd.read_csv('https://gist.githubusercontent.com/JuanFeA98/ce470cf42a2b4449a314adef81211bf5/raw/d014b5d9cd080d99af363c2e511e16a84fc92cf3/CSS_colors.csv')
df = pd.read_csv('https://gist.githubusercontent.com/JuanFeA98/0bfa884584ec80d241bf28d02eab0fdf/raw/d269b98814a4393b19673b5c56210e699223c926/titanic.csv')
# print(len(df))

# data = dict(df.iloc[0])
# data = (list(data.values()))
# data = data['PassengerId', 'Survived']
# print(data)
# db.collection('titanic').document(f'color_{1}').set(data)

for i in range(10):
    data = dict(df.iloc[i])
    print(data)
    # print(data['PassengerId'])
    db.collection('titanic').document(f'CODE_{data["PassengerId"]}').set(data)



# Imprimir la primera fila del dataset
# for i in range(1):
#     print(i)
#     data = dict(df.iloc[i])
#     print(data)
#     db.collection('titanic').add(data)

    # db.collection('titanic').document(1).set(data)