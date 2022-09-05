from firebase import firebase
firebase = firebase.FirebaseApplication("https://console.firebase.google.com/u/0/project/face-1851e", None)
data = {
    'Name': 'Esther',
    'email': 'par@gmail.com',
    'phone ': '056789066',
}
result = firebase.post('/facerecognition/Customer', data)
print(result)
