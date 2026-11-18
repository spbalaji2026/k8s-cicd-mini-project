from flask import Flask
import socket

app = Flask(__name__)

VERSION = "1"  # change this number later to see CI/CD in action


@app.route("/")
def home():
    return (
        f"<h1>Hello from Kubernetes! Version {VERSION}</h1>"
        f"<p>Served by pod: {socket.gethostname()}</p>"
    )


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
