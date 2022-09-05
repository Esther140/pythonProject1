import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('face-1851e-firebase-adminsdk-5a1v3-74950662a6.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://face-1851e-default-rtdb.firebaseio.com/"
	})


database_reference = db.reference("/")

with open("employee_details.json", "r") as f:
	file_contents = json.load(f)
database_reference.set(file_contents)