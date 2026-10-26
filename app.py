
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, DVP Week 12!</h1><p>My Jenkins CI/CD pipeline is working.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
