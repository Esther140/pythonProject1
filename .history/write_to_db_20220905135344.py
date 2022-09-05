from firebase_admin import db
import json

database_reference = db.reference("/employee-faces")

with open("employee_details.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)