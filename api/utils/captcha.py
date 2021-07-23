import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


CAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"



def is_valid_captcha(token, captcha_secret=None):
    captcha_secret = captcha_secret or get_captcha_secret()
    response = requests.post(CAPTCHA_VERIFY_URL, {
        "secret": captcha_secret,
        "response": token,
    })
    return response.json().get('success')


def get_captcha_secret():
    if not hasattr(settings, 'CAPTCHA_SECRET'):
        raise ImproperlyConfigured('CAPTCHA_SECRET is not set in settings file.')
    return settings.CAPTCHA_SECRET