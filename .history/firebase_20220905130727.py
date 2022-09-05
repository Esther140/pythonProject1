import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':databaseURL
	})