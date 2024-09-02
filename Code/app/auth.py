from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

bp = Blueprint('auth', __name__)

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if User.query.get(data['username']):
        return jsonify({"message": "User already exists"}), 400
    
    user = User(id=data['username'], username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.get(data['username'])
    if user and user.check_password(data['password']):
        # Generate a token or session (this is just a placeholder)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401
