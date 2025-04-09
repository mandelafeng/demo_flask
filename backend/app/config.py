class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost:3306/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your-secret-key-here'