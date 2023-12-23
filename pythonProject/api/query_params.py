from flask import Flask, request

app = Flask(__name__)


@app.get("/<details>")
def landing_page(details):
    if details == 'user':
        fn = request.args.get('fn')
        ln = request.args.get('ln')
        response = "Welcome " + fn + " " + ln
    elif details == 'address':
        city = request.args.get('city')
        state = request.args.get('state')
        response = "Location captured as " + city + " " + state
    elif details == 'number':
        ph = request.args.get('ph')
        response = "Contact at " + ph

    return response


if __name__ == '__main__':
    app.run(port=8080, debug=True)
