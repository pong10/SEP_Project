import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("parcel-express-9ffc9-firebase-adminsdk-sqntg-0f018e07b8.json")
default_app = firebase_admin.initialize_app(cred)
