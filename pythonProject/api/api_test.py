from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"jas": {"age": 39, "gender": "male"},
         "dil": {"age": 37, "gender": "female"},
         "srt": {"age": 8, "gender": "female"},
         "sdk": {"age": 5, "gender": "male"}}


class Home(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "posted successfully"}, 201


api.add_resource(Home, "/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)
