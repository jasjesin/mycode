from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256  # hashing algorith
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required, get_jwt, get_jwt_identity
from blocklist import BLOCKLIST


class Users:
    pass


users = Users()
user = [user for user in users]

blp = Blueprint("Users", "users", description="Operation on Users")


@blp.route("/register")
class UserRegister(MethodView):
    @jwt_required()
    def post(self, user_data):
        # check if username is unique, abort 409, if username alrdy exists
        password = pbkdf2_sha256.hash(user_data["password"])
        # db.session.add(user)
        # db.session.commit()
        return {"message": "user created successfully"}, 201


@blp.route("/user")  # Flask endpoint, avl at http://127.0.0.1:8080/user
class UserRegister(MethodView):
    def get(self):  # function associated with endpoint
        return {"users": list(users.values())}


@blp.route("/users/<string:user_id>")
class DeleteUser(MethodView):
    jwt = get_jwt()
    if not jwt.get("is_admin"):  # jwt.get allows to look any info stored in JWT
        abort(401, message="Admin privilege reqd")

    def delete(user_id):
        try:
            del users[user_id]
            return {"message": "user deleted."}
        except KeyError:
            abort(404, message="user not found")


@blp.route("/login")
class UserLogin(MethodView):
    @jwt_required()
    def post(self, user_data):
        if user_data["name"] not in users["name"]:
            abort(404, message="user not found")
        if pbkdf2_sha256.hash(user_data["password"]) == users["password"]:
            # Here we compare if stored & provided hashed password match
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}
        abort(401, "invalid password.")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)  # this tells require refresh token, NOT fresh access token
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, refresh=False)
        return {"access_token": new_token}


@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):                 # grab JWT's JTI n add it to blocklist
        jti = get_jwt().get("jti")
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}
        

