from .base import *

DEBUG = False
ALLOWED_HOSTS = ['bgmnbear.com', 'www.bgmnbear.com']

INSTALLED_APPS += [
    'api',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
