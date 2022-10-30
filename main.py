from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def hello_world():
    return {
        "slackUsername": "Lateefah",
        "backend": True,
        "age": 19,
        "bio": "Backend Developer"

    }


if __name__ == "__main__":
    app.run(debug=True)
