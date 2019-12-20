import firebase_admin
from firebase_admin import credentials, firestore, storage, auth

cred = credentials.Certificate("privateKey/gltf-storage-firebase-adminsdk-b3kbp-8952bc56e8.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'gltf-storage.appspot.com'})
db = firestore.client()
bucket = storage.bucket()
blob = bucket.blob('hello.txt')

# Initialize the default app
print("uploading to gs://" + bucket.name)  # "[DEFAULT]"

outfile='C:\\Users\\Riccardo\\Desktop\\hello.txt'
with open(outfile, 'rb') as my_file:
    blob.upload_from_file(my_file)
