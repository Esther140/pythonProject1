from firebase_admin import db
import json

database_reference = db.reference("/")

with open("employee_details.json", "r") as f:
	file_contents = json.load(f)
database_reference.set(file_contents)