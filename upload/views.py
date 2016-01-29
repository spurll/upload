from os import path, listdir
from string import ascii_letters, digits, punctuation
from random import choice
from flask import render_template, flash, session
from flask.ext.wtf import Form
from wtforms.fields import FileField, PasswordField
from wtforms.validators import Required, ValidationError

from upload import app
from upload.mailbox import Mailbox


class UploadForm(Form):
    file_field = FileField(validators=[Required()])
    password = PasswordField("Password:")

    def validate_password(form, field):
        if app.config['REQUIRE_PASSWORD']:
            password = open(app.config['PASSWORD_FILE'], 'r').read()
            if field.data != password:
                print('Invalid password: {}'.format(field.data))
                raise ValidationError('Invalid password.')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.is_submitted():
        if form.validate_on_submit() and available():
            try:
                filename = form.file_field.data.filename
                form.file_field.data.save(
                    path.join(app.config['FILEPATH'], filename)
                )

                flash('{} uploaded successfully.'.format(filename))

                # Send notification email if email provided.
                if app.config['NOTIFY']:
                    notify(filename)

            except Exception as e:
                flash('An error occurred during upload: {}'.format(e))
                raise

            # Generate new password.
            password = generate_password()
            print('New password: {}'.format(password))
            open(app.config['PASSWORD_FILE'], 'w').write(password)

        else:
            if available():
                flash('Unable to validate: {}'.format(form.errors))

    return render_template('index.html', form=form, available=available())

def generate_password(length=30):
    return ''.join(
        choice(ascii_letters + digits + punctuation) for i in range(length)
    )

def available():
    return not app.config['LIMIT_FILES'] or not listdir(app.config['FILEPATH'])
 
def notify(name):
    mailbox = Mailbox(app.config['USERNAME'], app.config['PASSWORD'],
                      app.config['SMTPHOST'])

    mailbox.send(
        [app.config['NOTIFY']],
        'A new file has been uploaded to the server: ' + name,
        'Upload'
    )
