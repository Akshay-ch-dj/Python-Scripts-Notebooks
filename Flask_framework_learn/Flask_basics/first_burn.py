from flask import Flask, redirect, url_for, render_template

# Instance of the flask web app
app = Flask(__name__)

# Home page


@app.route("/<show>")
def home(show):
    return render_template("index.html", content=show)


@app.route("/user/<name>")
def user(name):
    return f'Hello {name}'


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Access prohibited!"))


# Run the app
if __name__ == "__main__":
    app.run()
