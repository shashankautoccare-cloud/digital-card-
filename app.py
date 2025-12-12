from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("employees.json", "r") as f:
        data = json.load(f)
    return render_template("index.html", emp=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
