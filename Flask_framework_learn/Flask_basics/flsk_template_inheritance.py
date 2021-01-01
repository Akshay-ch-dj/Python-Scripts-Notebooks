from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", content="Testing")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # If the page is loaded with POST, name for the input
        user = request.form["nm"]
        # Use this information and redirect to the user page
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


# Run in debug mode
if __name__ == "__main__":
    app.run()
