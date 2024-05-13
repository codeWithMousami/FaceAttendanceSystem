import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://faceattendancerealtime-e6fd6-default-rtdb.firebaseio.com/'})

ref =db.reference('Students')


data = {

    '333333':
        {
            'name': 'Mousami Sanyal',
            'major': 'Data Science',
            'starting_year': 2023,
            'total_attendance':6,
            'standing':'A',
            'year': 2,
            'last_attendance':'2024-03-31 00:54:34'


        },
    '852741':
        {
            'name': 'Emly Blunt',
            'major': 'Theatre',
            'starting_year': 2020,
            'total_attendance':3,
            'standing':'C',
            'year': 1,
            'last_attendance':'2024-03-31 00:54:34'


        },
    '963852':
        {
            'name': 'Elon Musk',
            'major': 'Economics',
            'starting_year': 2019,
            'total_attendance':4,
            'standing':'B',
            'year':4,
            'last_attendance':'2024-03-31 00:54:34'


        }
}

for key,value in data.items():
    ref.child(key).set(value)