CSRF_ENABLE = True
SECRET_KEY = 'apples'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'local_db.db')
