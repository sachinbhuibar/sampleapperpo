from flask import Flask
firstapp = Flask(__name__)


@firstapp.route("/")
def index():
    return "first service on port 3000"


if __name__ == "__main__":
    firstapp.run(host="0.0.0.0", port=3000)
