import uuid
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from scratch.api.setup_n_ops.db import stores
from scratch.api.setup_n_ops.schemas import StoreSchema

# Blueprint is used to divide an API into multiple segments

blp = Blueprint("stores", __name__, description="operation on stores")


# This name, stores, in Blueprint is going to be referred if this Blueprint
# needs to be linked to another Blueprint. Each Blueprint has a unique __name__
# description goes into API documentation

# MethodView is used for creating class, whose methods route to specific endpoints
# 1 class per endpoint.
# Handling of multiple HTTP actions on same endpoint, defined in instance methods
# These instance methods are named same as HTTP Action names, i.e.,
#   get, post, put, delete etc, for HTTP action to match to method invocation

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="store not found")

# delete methods need NOT be decorated & these do not return anything that
# API deals with.
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "store deleted."}
        except KeyError:
            abort(404, message="store not found")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)  #order of decorator matters
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(404, message="Store already exists.")
        store_id = uuid.uuid4().hex
        new_store = {**store_data, "store_id": store_id}
        stores[store_id] = new_store
        return new_store, 201
