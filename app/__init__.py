from flask import Flask

def create_app(config_object):
    """Construct a Flask application"""
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)

    with flask_app.app_context():
        # Add routes
        from .routes import general

    return flask_app
