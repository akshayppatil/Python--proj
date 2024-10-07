# app/views/routes.py
from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController

# Create a Blueprint for routes
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    return jsonify(*UserController.signup(username, password))

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    return jsonify(*UserController.login(username, password))

@user_bp.route('/users/<username>', methods=['PUT'])
def update_user(username):
    data = request.json
    new_username = data.get('username')
    new_password = data.get('password')

    if not new_username or not new_password:
        return jsonify({'error': 'New username and password are required'}), 400

    return jsonify(*UserController.update_user(username, new_username, new_password))

@user_bp.route('/users/<username>', methods=['PATCH'])
def patch_user(username):
    data = request.json
    updates = {}

    if 'username' in data:
        updates['username'] = data['username']

    if 'password' in data:
        updates['password'] = data['password']

    if not updates:
        return jsonify({'error': 'Nothing to update'}), 400

    return jsonify(*UserController.patch_user(username, updates))
