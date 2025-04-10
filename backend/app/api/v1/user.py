from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required

from backend.app.common.response_body import response_body
from ...models.user import User

auth_bp = Blueprint('user', __name__, url_prefix='/v1/user')

@jwt_required()
@auth_bp.route('/info', methods=['GET'])
def get_user_by_username():
    return response_body(20000, "success", {"username": "admin"})