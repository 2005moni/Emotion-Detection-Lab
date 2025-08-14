"""Flask server for text validation web app."""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    """Handle GET and POST requests for the home page."""
    message = ""
    if request.method == "POST":
        text = request.form.get("text")
        if not text or text.strip() == "":
            message = "Invalid text, please try again"
        else:
            message = f"You entered: {text}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
