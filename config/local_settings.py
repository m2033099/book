import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7#whkl8p%!(z1fqopt!!sc(gg=&*#muer^1evhy75)dt^65$lz'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mayamayuki',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True

ANYMAIL = {
    "MAILGUN_API_KEY": "a34da71e9812ad5078111fefe53ed909-28d78af2-49546361",
    "MAILGUN_SENDER_DOMAIN": 'sandboxcf83f5110be441f39437995eb8cab928.mailgun.org',
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "recommend_book@example.com"
SERVER_EMAIL = "m1610600@gmail.com"
