import os
from flask import render_template, flash, session
from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms.validators import Required

from upload import app
from upload.mailbox import Mailbox


class UploadForm(Form):
    file_field = FileField(validators=[Required()])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.is_submitted():
        if form.validate_on_submit() and available():
            try:
                filename = form.file_field.data.filename
                form.file_field.data.save(
                    os.path.join(app.config['FILEPATH'], filename)
                )

                flash('{} uploaded successfully.'.format(filename))

                # Send notification email if email provided.
                if app.config['NOTIFY']:
                    notify(filename)

            except Exception as e:
                flash('An error occurred during upload: {}'.format(e))
                raise

        else:
            if available():
                flash('Unable to validate file.')

    return render_template('index.html', form=form, available=available())

def available():
    return (
        not app.config['LIMIT_FILES'] or not os.listdir(app.config['FILEPATH'])
    )
 
def notify(name):
    mailbox = Mailbox(app.config['USERNAME'], app.config['PASSWORD'],
                      app.config['SMTPHOST'])

    mailbox.send(
        [app.config['NOTIFY']],
        'A new file has been uploaded to the server: ' + name,
        'Upload'
    )
