from .base import *

ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'monet_db',
        'USER': 'monet_user',
        'PASSWORD': 'monet_pass',
    }
}