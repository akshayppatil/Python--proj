# app/controllers/user_controller.py
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user_model import UserModel

class UserController:
    @staticmethod
    def signup(username, password):
        hashed_password = generate_password_hash(password)
        try:
            UserModel.create_user(username, hashed_password)
            return {'message': 'User created successfully'}, 201
        except Exception:
            return {'error': 'Username already exists'}, 400

    @staticmethod
    def login(username, password):
        user = UserModel.find_user_by_username(username)
        if user is None or not check_password_hash(user[1], password):
            return {'error': 'Invalid username or password'}, 400
        return {'message': 'Login successful'}, 200

    @staticmethod
    def update_user(username, new_username, new_password):
        hashed_password = generate_password_hash(new_password)
        updated = UserModel.update_user(username, new_username, hashed_password)
        if updated == 0:
            return {'error': 'User not found'}, 404
        return {'message': 'User updated successfully'}, 200

    @staticmethod
    def patch_user(username, updates):
        if 'password' in updates:
            updates['password'] = generate_password_hash(updates['password'])

        updated = UserModel.partial_update_user(username, updates)
        if updated == 0:
            return {'error': 'User not found'}, 404
        return {'message': 'User updated successfully'}, 200
