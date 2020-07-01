from flask import Flask, render_template, session
import sqlite3

app = Flask(__name__)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"

app_reviews = {
    "1": {
        "title": "Lorem ipsum",
        "slogan": "There is no one who loves pain itself",
        "icon": "hurt.png",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec vehicula felis. Suspendisse sollicitudin ante lacus, ac mattis odio elementum et. Vivamus sit amet efficitur odio. Sed commodo auctor massa, in eleifend lectus porta sed. Maecenas id massa eleifend, tincidunt mi sed, sagittis erat. Nullam volutpat, arcu a rhoncus ultrices, lectus libero hendrerit odio, sed vehicula nisl dolor ac lectus. Praesent posuere eros quis ligula pharetra facilisis. Duis dictum eu dui eu sagittis. Suspendisse et risus in nunc imperdiet ultricies. Nam at augue quis enim venenatis fermentum eu accumsan neque. Maecenas porta mauris massa, sit amet commodo augue auctor sed. Donec congue at libero at tincidunt. Sed tristique ac diam ut convallis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam ut felis sit amet nunc tincidunt vestibulum. Mauris rhoncus mattis volutpat. Nulla vitae lacus et lacus porttitor lacinia. Etiam non ante ut elit cursus tincidunt. Aenean nec nulla pulvinar, dignissim eros nec, consectetur lorem. Suspendisse iaculis tortor id nibh consequat, eget efficitur enim fermentum. Sed ac mi sit amet dui cursus volutpat sed id nulla. Maecenas malesuada neque vitae orci efficitur bibendum. Vivamus ac nisi posuere elit egestas varius vitae ac lacus",
        "next": "2"
    },
    "2": {
        "title": "reliefQ",
        "slogan": "see what matters.",
        "icon": "heart.png",
        "description": "reliefQ raises funds from its charitable users for the causes currently in the most need. Organizations create a profile with reliefQ and share statistics such as humanitarian impact, charitable commitment, fundraising efficiency, and current demand of their cause/charity. Our algorithm measures and compares these factors and promotes charities of the most need to the top of the reliefQ. Organizations of exceptional need can be “prompted” to the top of reliefQ by developers.",
        "next": "3"
    },
    "3": {
        "title": "Aaaarrrrgggghhhh!",
        "slogan": "cleave him to the brisket!!!!!!!",
        "icon": "pirate.png",
        "description": "What in Davy Jones’ locker did ye just bark at me, ye scurvy bilgerat? I’ll have ye know I be the meanest cutthroat on the seven seas, and I’ve led numerous raids on fishing villages, and [censored] over 300 wenches. I be trained in hit-and-run pillaging and be the deadliest with a pistol of all the captains on the high seas. Ye be nothing to me but another source o’ swag. I’ll have yer guts for garters and keel haul ye like never been done before, hear me true. You think ye can hide behind your newfangled computing device? Think twice on that, scallywag. As we parley I be contacting my secret network o’ pirates across the sea and yer port is being tracked right now so ye better prepare for the typhoon, weevil. The kind o’ monsoon that’ll wipe ye off the map. You’re sharkbait, fool. I can sail anywhere, in any waters, and can kill ye in o’er seven hundred ways, and that be just with me hook and fist. Not only do I be top o’ the line with a cutlass, but I have an entire pirate fleet at my beck and call and I’ll [censored] sure use it all to wipe yer [censored] off o’ the world, ye dog. If only ye had had the foresight to know what devilish wrath your jibe was about to incur, ye might have belayed the comment. But ye couldn’t, ye didn’t, and now ye’ll pay the ultimate toll, you buffoon. I’ll [censored] fury all over ye and ye’ll drown in the depths o’ it. You’re fish food now.",
        "next": "3"
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

@app.route("/review/results", strict_slashes=False)
def results():
    return render_template("results.html", approved_apps=approved_apps, rejected_apps=rejected_apps)
