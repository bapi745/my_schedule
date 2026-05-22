from flask import Flask
from flask_jwt_extended import JWTManager
from config.settings import Config
from .models.db import db
from .routes.auth import auth_bp
from .routes.tasks import tasks_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

    # Create all tables on startup
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return {
            "message": "Task Manager API",
            "version": "1.0.0",
            "endpoints": {
                "auth": {
                    "register": "POST /api/auth/register",
                    "login": "POST /api/auth/login",
                    "me": "GET /api/auth/me"
                },
                "tasks": {
                    "create": "POST /api/tasks/",
                    "get_all": "GET /api/tasks/",
                    "get_one": "GET /api/tasks/<id>",
                    "update": "PUT /api/tasks/<id>",
                    "delete": "DELETE /api/tasks/<id>"
                }
            }
        }

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)