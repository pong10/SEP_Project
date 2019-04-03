'''
import json
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('‪parcel-express-9ffc9-export (1).json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://parcel-express-9ffc9.firebaseio.com/'})
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('‪parcel-express-9ffc9-0d06f93bf4bd.json')
firebase_admin.initialize_app(cred)

db = firestore.client()