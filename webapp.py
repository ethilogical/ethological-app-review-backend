from flask import Flask, render_template, session
import sqlite3

app = Flask(__name__)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"

def get_app_reviews():
    con = sqlite3.connect("database.sqlite")
    cur = con.cursor()
    cur.execute("""
        SELECT id, title, slogan
        FROM app_review
        """)

    # get the results as a list
    results = list(cur)
    # disconnect from the database
    con.close()
    # display the results (using column indexes)
    return results

@app.route("/", strict_slashes=False)
@app.route("/restore/<hash>", strict_slashes=False)
def show_review(hash=None):
    #get_app_reviews()
    app_review = {
        "title":"reliefQ",
        "slogan": "see what matters."
    }
    return render_template("review.html", app_review=app_review)
