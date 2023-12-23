import uuid
from flask import Flask, request
from scratch.api.setup_n_ops.db import stores, items
from flask_smorest import abort

app = Flask(__name__)  # creates flask app for us


# Here we have moved away from lists n started using dictionary
# This helps reference store n items wid UUID. This is how it works in DB as well


@app.get("/store")  # Flask endpoint, avl at http://127.0.0.1:8080/store
def get_all_stores():  # function associated with endpoint
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():  # code the endpoint by writing fn body abt how to store data
    store_data = request.get_json()
    if "name" not in store_data:
        abort(404, message="Bad request. Ensure 'name' is included in JSON payload.")
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(404, message="Store already exists.")
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "store_id": store_id}
    stores[store_id] = new_store
    return new_store, 201


# data can be sent by client, in URL, query pmtrs or header or body


@app.get("/item")  # Flask endpoint, avl at http://127.0.0.1:8080/store
def get_all_items():  # function associated with endpoint
    return {"items": list(items.values())}


@app.post("/item")
def create_item():
    item_data = request.get_json()  # grab incoming json data
    if ("price" or "name" or "store_id") not in item_data:
        abort(400, message="Bad request. Ensure 'name', 'price' and 'store_id "
                           "are mentioned in JSON payload")
    for item in items.values():
        if (item_data["name"] == item["name"]) and (item_data["store_id"] == item["store_id"]):
            abort(404, message="item already exists in the store")
    if item_data["store_id"] not in stores:
        abort(404, message="store not found")
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "item_id": item_id}
    items[item_id] = new_item
    return new_item, 201


# Design decisions like what if 2 stores have same name, give unique storeID
# What is data sent by client is incorrect?


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="store not found")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "store deleted."}
    except KeyError:
        abort(404, message="store not found")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="item not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "item deleted."}
    except KeyError:
        abort(404, message="item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    #    if request.is_json:
    item_data = request.get_json()
    if ("name" or "price") not in item_data:
        abort(404, message="Bad request. Ensure 'name' and 'price' "
                           "are present in JSON payload")
    try:
        item = items[item_id]
        item |= item_data
        return item
    except KeyError:
        abort(404, message="item not found")


#    abort(400, message="Request is not in valid JSON format.")


if __name__ == '__main__':
    app.run(port=8080, debug=True)  # any data requested to URL generated wid this
    #                                 will be intercepted by Flask app n do
    #                                 something with it. At the moment it will
    #                                 return 404 as no method is defined yet.

# What is JSON (JavaScript Object Notation) ?
# REST APIs usually work wid JSON. u recv JSON data in request n u respond wid
# JSON data in response. JSON is a long string of data. Its just text.
# But the contents follow a specific format so that client can then understand
# what is inside it. JSON contains key-value pairs, dont need to be ordered.
# We return dictionary to Flask & Flask turns it into JSON for us (it stringifies)
#
# Blueprints and MethodViews
# Blueprint is used to divide an API into multiple segments
