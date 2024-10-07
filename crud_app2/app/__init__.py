# app/__init__.py
from flask import Flask
from app.views.routes import user_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(user_bp)

    return app
