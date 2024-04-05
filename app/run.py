from config import db, init_app
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from routes import create_routes
from swagger import swagger_json

from flask import Flask

app = Flask(__name__)
api = Api(app)

# Initialize app with configuration
init_app(app)

# Call create_routes function to define routes
create_routes(api)

# Blueprint for Swagger UI
SWAGGER_URL = "/api/docs"
API_URL = "/api/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Product API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

with app.app_context():
    db.create_all()


@app.route("/api/swagger.json")
def get_swagger():
    return swagger_json()


if __name__ == "__main__":
    app.run(debug=True)
