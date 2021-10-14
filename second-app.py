from flask import Flask
secondapp = Flask(__name__)


@secondapp.route("/")
def index():
    return "second service on port 4000"


if __name__ == "__main__":
    secondapp.run(host="0.0.0.0", port=4000)
