# auth.py
users = {"admin": "password123"}  # Example user database

def authenticate_user(username, password):
    return users.get(username) == password
