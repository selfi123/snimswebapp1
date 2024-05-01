from firebase_admin import credentials,firestore,auth
import firebase_admin


cred = credentials.Certificate("firebase/flutter-hosmngment-firebase-adminsdk-dj8hb-40853f1068.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

users=auth.get_user('E4aNpsr3NMN2Sq0HNB2MjNgipzd2')
print(users.email.split('@')[0])