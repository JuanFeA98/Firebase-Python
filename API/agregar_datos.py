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
df = pd.read_csv('../Data/titanic.csv')
df = df.fillna(0)

for i in range(len(df)):
    pre_data = dict(df.iloc[i])

    data = {
        'PassengerId': int(pre_data['PassengerId']),
        'Survived': int(pre_data['Survived']),
        'Pclass': int(pre_data['Pclass']),
        'Name': str(pre_data['Name']),
        'Sex': str(pre_data['Sex']), 
        'Age': float(pre_data['Age']),
        'SibSp': int(pre_data['SibSp']),
        'Parch': int(pre_data['Parch']),
        'Ticket': str(pre_data['Ticket']),
        'Fare': float(pre_data['Fare']),
        'Cabin':str(pre_data['Cabin']),
        'Embarked': str(pre_data['Embarked'])
    }


    db.collection('titanic').document(f'{int(pre_data["PassengerId"])}').set(data)
