class Config:
    SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'


class Development(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/rehab'
    DEBUG = True
    JWT_SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'


class Production(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ''
    JWT_SECRET_KEY = '3b4c830cd7d88c05cfa5d6da59af4561'

    DEBUG = False