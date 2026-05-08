from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Added API route for your routes.json
@app.route("/api/routes")
def get_routes():
    try:
        with open("routes.json", "r") as file:
            data = json.load(file)
            return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "routes.json not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)