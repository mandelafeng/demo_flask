import importlib
import logging
import os
import sys

from flask import Flask, Blueprint
from app.config import Config, blueprint_modules
from app.common.error import handle_404_error, handle_500_error, handle_all_exceptions
from app.common.extensions import db, jwt
from dotenv import load_dotenv
# 获取项目根目录的路径
load_dotenv()

# 将项目根目录添加到 sys.path 中
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(project_root)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 开启 SQLAlchemy 的日志记录
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)

    # 注册蓝图
    for module_name in blueprint_modules:
        module = importlib.import_module(module_name)
        for attr in dir(module):
            if isinstance(getattr(module, attr), Blueprint):
                app.register_blueprint(getattr(module, attr))

    # 全局异常处理
    app.register_error_handler(404, handle_404_error)
    app.register_error_handler(500, handle_500_error)
    app.register_error_handler(Exception, handle_all_exceptions)
    # 创建数据库表
    with app.app_context():
        db.create_all()

    return app