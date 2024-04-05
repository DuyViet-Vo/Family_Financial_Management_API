from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()


def init_app(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:vdv1810@localhost/test_db_1"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "vdv1810"
    db.init_app(app)
    jwt.init_app(app)
