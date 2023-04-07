from flask import Flask

App = Flask(__name__)


@App.route("/")
def say_hi():
    return "<p>Hello API Week!</P>"


if __name__ == "__mian__":
    App.run(debug=True)
