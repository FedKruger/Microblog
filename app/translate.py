import json
import requests
from flask_babel import _
from app import app


def translate(text, lang):
    if 'YA_TRANSLATOR_KEY' not in app.config or \
            not app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'API_Key': app.config['YA_TRANSLATOR_KEY']}
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate'.format(
                         text, lang), headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))