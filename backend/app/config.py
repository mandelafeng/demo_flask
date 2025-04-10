class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5tgbnhY6!@localhost:3306/simple_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-secret-key-here'

blueprint_modules = [
    'app.api.v1.auth',
    'app.api.v1.user'
]