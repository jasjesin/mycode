from flask import Flask, request, jsonify

app = Flask(__name__)
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


def _find_next_id():
    # return max(country['id'] for country in countries) + 1
    next_id = len(countries) + 1
    return next_id


@app.get("/")
def home_page():
    return "Welcome Home!"


@app.get("/countries")
def get_countries():
    return jsonify(countries), 200


@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country['id'] = _find_next_id()
        countries.append(country)
        return country, 201
    return f'\nERROR: please verify and make sure that request is in correct JSON format', 415


@app.get("/countries/<country_id>")
def get_details_by_id(country_id):
    if countries[int(country_id)-1] in countries:
        return jsonify(countries[int(country_id)-1]), 200
    else:
        return f'\nThis ID {id} does not exist. Please enter valid ID', 404


if __name__ == '__main__':
    app.run(debug=True)
