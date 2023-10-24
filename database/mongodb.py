from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['kafka_db']

def store_user_data(user_data):
    db.users.insert_one(user_data)

def find_user_by_email(email):
    return db.users.find_one({'email': email})
