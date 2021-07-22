import django_heroku
from . import *

DEBUG = os.environ.get('DEBUG', 0)

django_heroku.settings(locals())

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
