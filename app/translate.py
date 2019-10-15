import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, lang):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = current_app.config['YA_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'.format(
        auth, text, lang))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8'))