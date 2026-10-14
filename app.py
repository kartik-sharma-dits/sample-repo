from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "message": "Hello World!",
        "status": "success",
        "platform": "Render"
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)