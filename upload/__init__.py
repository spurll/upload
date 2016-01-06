from flask import Flask
from os import path


app = Flask(__name__)
app.config.from_object('config')


from upload import views


# Password will be reset every time the server is.
if app.config['REQUIRE_PASSWORD']:
    open(app.config['PASSWORD_FILE'], 'w').write(views.generate_password())
