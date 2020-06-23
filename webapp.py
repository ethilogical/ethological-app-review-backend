from flask import Flask, render_template, session
import sqlite3

app = Flask(__name__)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"

app_reviews = {
    "1": {
        "title": "reliefQ",
        "slogan": "see what matters.",
        "icon": "heart.png",
        "next": "2"
    },
    "2": {
        "title": "reliefQRS",
        "slogan": "see what matters.12",
        "icon": "heart.png",
        "next": "3"
    }
}

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
