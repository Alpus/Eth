import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = '1HnsSJ6SnS8jSgS7SGAgq3'
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'public'
RECAPTCHA_PRIVATE_KEY = 'private'
RECAPTCHA_OPTIONS = {'theme': 'white'}