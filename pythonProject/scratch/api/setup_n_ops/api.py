from flask import Flask, request, jsonify, Blueprint, abort
from flask.views import MethodView

# Blueprints allow us to separate various endpoints into subdomains.

app = Flask(__name__)  # Create an instance of the class
stores = [
    {
        "name": "a",
        "items": [
         {
             "name": "chair",
             "price": 15.99
          }
        ]
     }
]

stores1 = [
    {
        "name": "Jas",
        "items": [
            {
                "name": "chair",
                "price": "13.99"
            }
        ]
    }
]


@app.get("/store1")
def get():
    return jsonify({"stores": stores1})


@app.get("/store")  # Flask endpoint, avl at http://127.0.0.1:8080/store
def get_stores():   # function associated with endpoint
    return {"stores": stores}


@app.post("/store1")
def post():
    data = request.get_json()
    new_data = {"name": data["name"], "items": []}
    stores1.append(new_data)
    return jsonify(new_data), 201


@app.post("/store")
def create_store():  # code the endpoint by writing fn body abt how to store data
    data = request.get_json()
    new_store = {"name": data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

# data can be sent by client, in URL, query pmtrs or header or body


@app.post("/store/<string:name>/item")
def create_item(name):
    data = request.get_json()  # grab incoming json data
    for store in stores:
        if store["name"] == name:
            new_item = {"name": data["name"], "price": data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404

# Design decisions like what if 2 stores have same name, give unique storeID
# What is data sent by client is incorrect?


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if store["name"] == name:
            return {"store": store["items"]}  # benefit: future extensible
        #  if we need to include additional data later on, can add in dictionary
        # Example: return {"store": store["items"], "new_data" : "extensible" }
    return {"message": "store not found"}, 404


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


