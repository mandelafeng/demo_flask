from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from backend.app.common.response_body import response_body
from backend.app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/v1/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # ...保持原有注册逻辑...

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400
    user = User.query.filter_by(username=username).first()
    print(user)
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401
    else:
        access_token = create_access_token(identity=user.username)
    return response_body(20000, "Login successful", {"token": access_token})
    # ...保持原有登录逻辑...