from utils import get_env_variable

POSTGRES_HOST = get_env_variable('POSTGRES_HOST')
POSTGRES_USER = get_env_variable('POSTGRES_USER')
POSTGRES_PASSWORD = get_env_variable('POSTGRES_PASSWORD')
POSTGRES_DB = get_env_variable('POSTGRES_DB')


class Config(object):
    uri_template = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'
    
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_PAGINATION_PER_PAGE = 10
       
    SQLALCHEMY_DATABASE_URI = uri_template.format(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        db=POSTGRES_DB)

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True