#!/usr/bin/env python
from app import application

application.debug = True

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
