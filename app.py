from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# Handle www redirect for SEO
@app.before_request
def redirect_nonwww():
    """Redirect non-www to www or vice versa for SEO consistency"""
    if request.url.startswith('http://') and not request.url.startswith('http://www.'):
        # Redirect http://domain.com to http://www.domain.com
        url = request.url.replace('http://', 'http://www.', 1)
        return redirect(url, code=301)

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