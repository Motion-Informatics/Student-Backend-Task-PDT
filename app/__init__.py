from flask import Flask
# Import blueprints for user routes
from app.routes.add_patient import add_patient_bp
from app.routes.add_user import add_user_bp
from app.routes.create_report import create_report_bp
from app.routes.setup_session import setup_session_bp


def create_app():
    app = Flask(__name__)
    
    # Register user blueprints
    app.register_blueprint(add_patient_bp)
    app.register_blueprint(add_user_bp)
    app.register_blueprint(create_report_bp)
    app.register_blueprint(setup_session_bp)

    return app