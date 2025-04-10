from flask import jsonify

def response_body(code, message, data=None):
    return jsonify({
        'code': code,
        'message': message,
        'data': data
    })