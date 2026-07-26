from flask import Flask

app = Flask(__name__)

VERSION = "v1"

@app.route("/")
def home():

    return {
        "application": "Blue-Green Demo",
        "version": VERSION
    }

@app.route("/health")
def health():

    return {
        "status": "healthy"
    }

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
