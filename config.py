class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:j0m04rm4@localhost/project_web'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER =  'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'arizamoises@gmail.com'
    MAIL_PASSWORD = 'f41ryt41l'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

