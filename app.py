from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

current_status = {
    "status": "UNKNOWN",
    "time": None
}

@app.route("/")
def index():
    return render_template(
        "index.html",
        status=current_status["status"],
        time=current_status["time"]
    )

@app.route("/update/<status>")
def update_status(status):
    current_status["status"] = status
    current_status["time"] = datetime.now().strftime("%d %b %Y, %H:%M:%S")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

