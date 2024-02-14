from flask import Flask

# tutorial: https://python-adv-web-apps.readthedocs.io/en/latest/flask.html

app = Flask(__name__)
app.config.from_prefixed_env()

import facereference.views
