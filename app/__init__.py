from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app