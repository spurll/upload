from os import urandom


# Web Server
CSRF_ENABLED = True
SECRET_KEY = urandom(30)
PROPAGATE_EXCEPTIONS = True

# Upload Options
FILEPATH = '/upload'
LIMIT_FILES = True          # If true, won't upload unless directory is empty.
SIZE_LIMIT = 1000000000     # File size in bytes.

# Notification Options
NOTIFY = None               # Email sent to this address when new file arrives.
USERNAME = 'your.email@gmail.com'
PASSWORD = 'app-specific-password'
SMTPHOST = 'smtp.gmail.com:587'
