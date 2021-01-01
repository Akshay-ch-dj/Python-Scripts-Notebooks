from datetime import timedelta
from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session,
    flash)

app = Flask(__name__)
app.secret_key = "mongoose"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html", content="Testing")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        # If the page is loaded with POST, name for the input
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!", "info")
        # Just redirect to the user page
        return redirect(url_for("user"))
    else:
        # To get to the logged in page as long as the session data exists
        if "user" in session:
            flash("Already Logged In", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    # Check if any session data exists, and login
    if "user" in session:
        user = session["user"]
        # Render the template with user value passed in
        return render_template("user.html", user=user)
    # If not valid session data, redirect back to the login page
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Check if the user logged in or not then display the flash message
    if "user" in session:
        user = session["user"]
        flash(f"You have been successfully logged out, {user}", "info")

    # For clearing out the session data
    session.pop("user", None)
    # Redirect to login page after that
    return redirect(url_for("login"))


# Run in debug mode
if __name__ == "__main__":
    app.run()
