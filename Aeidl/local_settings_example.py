DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Your database name',
        'USER': 'Your database user',
        'PASSWORD': 'Your database password',
        'HOST': 'localhost',
        'PORT': 5432,
        'CHARSET': 'UTF-8'
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your email'
EMAIL_HOST_PASSWORD = 'Your password'
