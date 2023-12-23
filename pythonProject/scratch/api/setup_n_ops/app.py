from flask import Flask
from flask_smorest import Api
from scratch.api.setup_n_ops.resources.item import blp as ItemBlueprint
from scratch.api.setup_n_ops.resources.store import blp as StoreBlueprint

app = Flask(__name__)


# The following entry informs that if there's an exception occurs inside an
# extension of Flask, to propagate into main app so that we can see it
app.config["PROPAGATE_EXCEPTIONS"] = True

# Following are flask-smorest configurations
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"

# OpenAPI is a standard for API documentation, specify which version to use
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"  # specified root of API

# swagger-ui path & URL, tells smorest to use swagger for API documentation
# URL specifies the swagger code, to be loaded from.
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)  # connects flask-smorest extension to Flask App
# The following are blp variables defined in store n item py files.
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)