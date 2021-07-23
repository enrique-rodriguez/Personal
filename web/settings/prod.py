import django_heroku
from . import *

DEBUG = os.environ.get('DEBUG', 0)

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())
