from flask import Flask, render_template
from app.estate.routes import estate

app = Flask(__name__)

app.register_blueprint(estate)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/shop')
def shop():
    return render_template('shop.html')


# 👇 keep this for local testing
if __name__ == "__main__":
    app.run(debug=True)