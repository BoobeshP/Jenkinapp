from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify(result=a + b)
    
@app.route("/")
def home():
    return "Flask app is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
