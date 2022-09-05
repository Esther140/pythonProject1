from  firebase import firebase
firebase = firebase.FirebaseApplication("https://foodapp-35dd5-default-rtdb.firebaseio.com/")
data = {
    'Name': 'Esther',
    'email': 'par@gmail.com',
    'phone ': '056789066',
}
result = firebase.post('/facerecognition/Customer', data)
print(result)
