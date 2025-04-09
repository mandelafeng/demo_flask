from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # ...保持原有注册逻辑...

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # ...保持原有登录逻辑...