import uuid
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from scratch.api.setup_n_ops.db import items, stores
from scratch.api.setup_n_ops.schemas import ItemSchema, ItemUpdateSchema

# Blueprint is used to divide an API into multiple segments

blp = Blueprint("items", __name__, description="operation on items")


# This name, stores, in Blueprint is going to be referred if this Blueprint
# needs to be linked to another Blueprint. Each Blueprint has a unique __name__
# description goes into API documentation

# MethodView is used for creating class, whose methods route to specific endpoints
# 1 class per endpoint.
# Handling of multiple HTTP actions on same endpoint, defined in instance methods


@blp.route("/item/<string:item_id>")  # multiple actions defined in methods, that can be performed for same endpoint
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "item deleted."}
        except KeyError:
            abort(404, message="item not found")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="item not found")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))  # casts into list n returns
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)  # This will validate incoming data format
    @blp.response(201, ItemSchema)
    def post(self, item_data):  # will contain JSON tht gets validated for fields
        # JSON that client sends, is passed thru ItemsSchema, which validates
        # for presence of mandatory fields & their associated data type and then
        # that schema gives this method, an argument, that is validated dictionary
        # Doing this also adds some more info to swagger UI documentation
        for item in items.values():
            # Marshmallow only checks incoming data, using defined structure. It
            # cannot verify data existence. So, following check remains here.
            if (item_data["name"] == item["name"]) and (item_data["store_id"] == item["store_id"]):
                abort(404, message="item already exists in the store")
        if item_data["store_id"] not in stores:
            abort(404, message="store not found")
        item_id = uuid.uuid4().hex
        new_item = {**item_data, "item_id": item_id}
        items[item_id] = new_item
        return new_item, 201

