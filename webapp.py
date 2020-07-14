from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299                     # taken from PA
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False            # taken from PA

app_reviews = {

}

approved_apps = [
    app_reviews["2"]
]

rejected_apps = [
    app_reviews["1"], app_reviews["3"]
]

def get_app_reviews():
    con = sqlite3.connect("database.sqlite")
    cur = con.cursor()
    cur.execute("""
        SELECT id, title, slogan, icon, next
        FROM app_review
        """)

    # get the results as a list
    results = list(cur)
    # disconnect from the database
    con.close()
    # display the results (using column indexes)
    return results

@app.route("/", strict_slashes=False)
def home():
    return render_template("home.html")

@app.route("/about", strict_slashes=False)
def about():
    return render_template("about.html")

@app.route("/review/app/", strict_slashes=False)
@app.route("/review/app/<app_id>", strict_slashes=False)
# @app.route("/review/<hash>", strict_slashes=False)
def show_review(app_id="1", hash=None):
    #get_app_reviews()
    
    return render_template("review.html", app_review=app_reviews[app_id])

# def show_review(app_id="2", hash=None):
#     #get_app_reviews()
    
#     return render_template("review.html", app_review=app_reviews[app_id])

# def show_review(app_id="3", hash=None):
#     #get_app_reviews()
    
#     return render_template("review.html", app_review=app_reviews[app_id])

@app.route("/review/app/results", strict_slashes=False)
def results():
    return render_template("results.html", approved_apps=approved_apps, rejected_apps=rejected_apps)
