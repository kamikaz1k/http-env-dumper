import os

from flask import Flask


app = Flask(__name__)


@app.route("/")
def dump():
    return {
        key: os.environ.get(key)
        for key in os.environ.keys()
    }


@app.route("/<env_var>")
def key(env_var):
    return {
        env_var: os.environ.get(env_var)
    }


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
