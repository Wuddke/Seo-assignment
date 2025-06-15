from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
@app.route("/pet-grooming-services")
def services():
    return render_template("services.html")

@app.route("/contact")
@app.route("/contact-us")
def contact():
    return render_template("contact.html")

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap_xml():
    return send_from_directory('static', 'sitemap.xml')

if __name__ == "__main__":
    app.run(debug=True)