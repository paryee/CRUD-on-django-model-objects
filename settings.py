# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'paryee@12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    'crud',
]

SECRET_KEY = 'SECRET KEY for this Django Project'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'