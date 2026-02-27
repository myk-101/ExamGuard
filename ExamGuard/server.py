from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/records")
def records():
    return render_template("records.html")

@app.route("/history")
def history():
    return render_template("history.html")



@app.route("/settings")
def settings():
    return redirect(url_for("account"))

@app.route("/settings/account")
def account():
    return render_template("settings/account.html")

@app.route("/settings/camera")
def camera_settings():
    return render_template("settings/camera.html")

@app.route("/settings/alerts")
def alerts_settings():
    return render_template("settings/alert.html")


@app.route("/settings/data&records")
def data_settings():
    return render_template("settings/data.html")

@app.route("/settings/change-password")
def changepass_settings():
    return render_template("settings/changepassword.html")


# ======================
# AUTH
# ======================

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


from waitress import serve

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)