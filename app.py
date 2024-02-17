from flask import Flask, abort

app = Flask(__name__)
counter = [0]  # Use a list so that the integer is mutable


@app.route("/")
def hello_world():
    counter[0] += 1
    if counter[0] % 10 == 0:
        abort(500)  # Return a 500 error
    return f"Hello, World! {counter[0]}"


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/world")
def world():
    return "World"


if __name__ == "__main__":
    app.run(port=8080, debug=True)
