import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7#whkl8p%!(z1fqopt!!sc(gg=&*#muer^1evhy75)dt^65$lz'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


ANYMAIL = {
    "MAILGUN_API_KEY": "c9ab78e169eb8280f80efa04c564746a-28d78af2-72e4e60b",
    "MAILGUN_SENDER_DOMAIN": 'sandbox1124c5806d5e43409705676438369f84.mailgun.org',
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "recommend_book@example.com"
SERVER_EMAIL = "m1610600@gmail.com"
