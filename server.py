from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def Main():
    return render_template("Main.html")

@app.route("/signup", methods=["GET"])
def Sign_Up():
    return render_template("Sign_Up.html")

@app.route("/login", methods=["GET"])
def Login():
    return render_template("Sign_Up.html")

@app.route("/junior", methods=["GET"])
def Junior():
    return render_template("Sign_Up.html")


@app.route("/senior", methods=["GET"])
def Senior():
    return render_template("Sign_Up.html")

@app.route("/faculty", methods=["GET"])
def Faculty():
    return render_template("Faculty_Dashboard.html")

@app.route("/room", methods=["GET"])
def Access_Room():
    return render_template("Access_Room.html")


if __name__ == "__main__":
    app.run(debug=True)
