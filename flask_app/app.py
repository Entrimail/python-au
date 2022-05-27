from datetime import datetime as dt
from flask import Flask, render_template
from generator import generate_password

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():   
        password = generate_password()
        return render_template(
            "index.html",
            title="Password Generator", password=password
            )

if __name__ == "__main__":
    app.run(debug=True)