from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pet-grooming-services")
def services():
    return render_template("services.html")



if __name__ == "__main__":
    app.run(debug=True)