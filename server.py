from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def Sign_Up():
    return render_template("Sign_Up.html")

if __name__ == "__main__":
    app.run(debug=True)
