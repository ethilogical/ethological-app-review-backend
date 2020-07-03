from flask import Flask, render_template, session
import sqlite3

app = Flask(__name__)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"

app_reviews = {
    "1": {
        "title": "City of Harrisonburg Police Department Warrant Planner",
        "slogan": "Integrity, Accountability, Honor, Leadership, Diversity",
        "icon": "warrant_icon.png",
        "preview": "warrant_preview.png",
        "description": "This app is only for use by liscensed officers of the City of Harrisonburg Police Department and may " +
                        "only be downloaded with affirmed consent from the City of Harrisonburg Police Department." +
                        "This app will be used to expedite the search for and booking of convicted criminals in the City of " +
                        "Harrisonburg area. When a warrant is issued for an individual's arrest, their description and identifying " +
                        "characteristics are automatically entered in to the app. Harrisonburg's facial detection system, enabled by " +
                        "traffic cameras on our major streets, will then be able to automatically locate, flag, and track any " +
                        "individual matching the description when they are seen by a camera. Officers logged in to the app " +
                        "can see the status of an arrest warrant and the location of any suspects. This innovative app will make " +
                        "for a more efficient police department and a safer City of Harrisonburg.",
        "result": "",
        "next": "2"
    },
    "2": {
        "title": "reliefQ",
        "slogan": "see what matters.",
        "icon": "reliefQ_icon.png",
        "preview": "reliefQ_preview.png",
        "description": "reliefQ raises funds from its charitable users for the causes currently in the most need. Organizations "
                        + "create a profile with reliefQ and share statistics such as humanitarian impact, charitable commitment, "
                        + " fundraising efficiency, and current demand of their cause/charity. Our algorithm measures and compares "
                        + "these factors and promotes charities of the most need to the top of the reliefQ. Organizations of "
                        + "exceptional need can be “prompted” to the top of reliefQ by developers.",
        "result": "",
        "next": "3"
    },
    "3": {
        "title": "Unmasked Unmasker",
        "slogan": "Protect yourself.",
        "icon": "unmasked_icon.png",
        "preview": "unmasked_preview.png",
        "description": "The Virginia state government is distributing this app as a part of it's ordinance that "
                        + "individuals of age 10 and up must wear face coverings in public. State residents who "
                        + "report unmasked individuals who can be correctly identified will be financially "
                        + "compensated. We hope that, by citizens policing each other, it will encourage more "
                        + "individuals to follow face covering ordinances in public.",
        "result": "",
        "next": "results"
    }
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
def show_review(app_id="1", hash=None):
    #get_app_reviews()
    
    return render_template("review.html", app_review=app_reviews[app_id])

# def show_review(app_id="2", hash=None):
#     #get_app_reviews()
    
#     return render_template("review.html", app_review=app_reviews[app_id])

# def show_review(app_id="3", hash=None):
#     #get_app_reviews()
    
#     return render_template("review.html", app_review=app_reviews[app_id])

@app.route("/review_1/app/", strict_slashes=False)
@app.route("/review_1/app/<app_id>", strict_slashes=False)
def show_review_1(app_id="1", hash=None):
    return render_template("review_1.html", app_review=app_reviews[app_id])

@app.route("/review_2/app/", strict_slashes=False)
@app.route("/review_2/app/<app_id>", strict_slashes=False)
def show_review_2(app_id="1", hash=None):
    return render_template("review_2.html", app_review=app_reviews[app_id])

@app.route("/review_3/app/", strict_slashes=False)
@app.route("/review_3/app/<app_id>", strict_slashes=False)
def show_review_3(app_id="1", hash=None):
    return render_template("review_3.html", app_review=app_reviews[app_id])

@app.route("/review_1/app/results", strict_slashes=False)
@app.route("/review_2/app/results", strict_slashes=False)
@app.route("/review_3/app/results", strict_slashes=False)
@app.route("/review/app/results", strict_slashes=False)
def results():
    return render_template("results.html", approved_apps=approved_apps, rejected_apps=rejected_apps)
