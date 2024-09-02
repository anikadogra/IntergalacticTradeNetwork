from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes
    from . import auth  # Import the auth blueprint

    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp, url_prefix='/api')  # Register auth blueprint with URL prefix

    return app
