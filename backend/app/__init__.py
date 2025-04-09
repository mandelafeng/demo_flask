from flask import Flask
from config import Config
from extensions import db, jwt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)

    # 注册蓝图
    from api.v1.auth import auth_bp
    app.register_blueprint(auth_bp)

    # 创建数据库表
    with app.app_context():
        db.create_all()

    return app