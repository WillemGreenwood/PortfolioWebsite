from os import environ

class Config:
    DEBUG = environ.get('FLASK_DEBUG', 0)
    SEND_FILE_MAX_AGE_DEFAULT = 0 if environ.get('FLASK_DEBUG', 0) else 43200  # Stop flask from caching files while debugging
