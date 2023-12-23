from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from scratch.api.setup_n_ops.resources.item import blp as ItemBlueprint
from scratch.api.setup_n_ops.resources.store import blp as StoreBlueprint
import secrets
app = Flask(__name__)
from scratch.api.auth_jwt.blocklist import BLOCKLIST

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


jwt = JWTManager(app)  # create an instance of JWTManager
# Also, we need to set a secret key, for signing JWTs.
# wen a user sends back a JWT to tell us who they are, our app can check
# secret key & can use it to verify that this app generated that JWT &
# therefore, that JWT is valid. So, basically, secret key is used to make
# sure that user hasn't created their own JWT somewhr else & is pretending
# to be JWT that our API generated. It prevents tampering wid JWT.
# As JWTs store info, we don't want user to be able to modify that info
# & send us back, pretending like it was us who created that JWT
app.config["JWT_SECRET_KEY"] = "jasjesin" # think of way to pull this from vault
# generate a long random secret key from some secret key generation s/w & use it
# In python, we can import secrets n pass in the length like this >>
# app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)
# secret key shouldnt be changed each time app is restarted, but this method will
# re-generate secret key wid each restart. So, better to generate it at terminal
# and then hard-code it here or store in vault n think of how to pull from there.

# JWT Claims and Authorization
# claim is saved wen JWT is created, NOT wen its used.
# so, if a user was an admin during JWT creation time but his admin access was
# revoked later on, JWT for him will still work as admin, till user logs in again
# so best to check latest access from DB/IAM, rather than storing it in claims


@jwt.additional_claims_loader()   # this runs each time a JWT is created
def add_claims_to_jwt(identity):  # this identity comes from create access token
    #                               method in user.py, that recvs identity pmtr
    if identity == "1":  # correct way, look in DB or IAM for access lvl
        return {"is_admin": True}   # helps provide admin access to specific work
    return {"is_admin": False}      # like deleting an item can need admin access


@jwt.needs_fresh_token_loader()
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({"message": "The token is not fresh",
                    "error": "fresh_token_required"}), 401

# to add or validate against list of terminated tokens


@jwt.token_in_blocklist_loader()
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST

# when above function returns TRUE, to define wht error message,
# will the user get, for terminated token; following fn will send msg to user


@jwt.revoked_token_loader()
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"description": "this token has been revoked",
                    "error": "token_revoked"}), 401

# Error Handling wid JWTs for JWT to be:
# - expired:


@jwt.expired_token_loader()  # returns a tuple wid a JSON n status code
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"message": "token has expired",
                    "error": "token_expired"}), 401

# following two functions are processed when there is NO JWT or invalid JWT
# - invalid: if client tries to change contents of JWT but they do not have secret key, then JWT gets invalid


@jwt.invalid_token_loader()
def invalid_token_callback(error):
    return jsonify({"message": "signature verification failed",
                    "error": "invalid_token"}), 401

# - required: JWT is required but not provided for protected endpoint


@jwt.unauthorized_loader()
def missing_token_callback(error):
    return jsonify({"message": "Request does not contain access token",
                    "error": "authorization_required"}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)