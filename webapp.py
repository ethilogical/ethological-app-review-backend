from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import datetime
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# we only need this if we want to start doing stuff with the session
app.config['SECRET_KEY'] = "someth1ng super secret and maybe even rand0m"
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299                     # taken from PA
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False            # taken from PA


class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    icon_url = db.Column(db.Text, nullable=False)
    preview_url = db.Column(db.Text, nullable=False)
    slogan = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    next = db.Column(db.Integer, nullable=True)


def seed_apps():
    print("seeding apps...")
    app0 = App(title="City of Harrisonburg Police Department Warrant Planner",
               icon_url="warrant_icon.png",
               preview_url="warrant_preview.png",
               slogan="Integrity, Accountability, Honor, Leadership, Diversity",
               description="This app is only for use by liscensed officers of the City of Harrisonburg Police Department and may " +
               "only be downloaded with affirmed consent from the City of Harrisonburg Police Department." +
                        "This app will be used to expedite the search for and booking of convicted criminals in the City of " +
                        "Harrisonburg area. When a warrant is issued for an individual's arrest, their description and identifying " +
                        "characteristics are automatically entered in to the app. Harrisonburg's facial detection system, enabled by " +
                        "traffic cameras on our major streets, will then be able to automatically locate, flag, and track any " +
                        "individual matching the description when they are seen by a camera. Officers logged in to the app " +
                        "can see the status of an arrest warrant and the location of any suspects. This innovative app will make " +
                        "for a more efficient police department and a safer City of Harrisonburg.")

    app1 = App(title="reliefQ",
               icon_url="reliefQ_icon.png",
               preview_url="reliefQ_preview.png",
               slogan="see what matters.",
               description="reliefQ raises funds from its charitable users for the causes currently in the most need. Organizations "
               + "create a profile with reliefQ and share statistics such as humanitarian impact, charitable commitment, "
                        + " fundraising efficiency, and current demand of their cause/charity. Our algorithm measures and compares "
                        + "these factors and promotes charities of the most need to the top of the reliefQ. Organizations of "
                        + "exceptional need can be promoted to the top of reliefQ by developers.")

    app2 = App(title="Lorem ipsum",
               icon_url="placeholder_icon.png",
               preview_url="placeholder.png",
               slogan="There is no one who loves pain itself",
               description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec vehicula felis. "
               + "Suspendisse sollicitudin ante lacus, ac mattis odio elementum et. Vivamus sit "
                        + "amet efficitur odio. Sed commodo auctor massa, in eleifend lectus porta sed. Maecenas "
                        + "id massa eleifend, tincidunt mi sed, sagittis erat. Nullam volutpat, arcu a rhoncus "
                        + "ultrices, lectus libero hendrerit odio, sed vehicula nisl dolor ac lectus. Praesent "
                        + "posuere eros quis ligula pharetra facilisis. Duis dictum eu dui eu sagittis. Suspendisse "
                        + "et risus in nunc imperdiet ultricies. Nam at augue quis enim venenatis fermentum eu "
                        + "accumsan neque. Maecenas porta mauris massa, sit amet commodo augue auctor sed. Donec "
                        + "congue at libero at tincidunt. Sed tristique ac diam ut convallis. Class aptent taciti "
                        + "sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam ut felis sit "
                        + "amet nunc tincidunt vestibulum. Mauris rhoncus mattis volutpat. Nulla vitae lacus et "
                        + "lacus porttitor lacinia. Etiam non ante ut elit cursus tincidunt. Aenean nec nulla pulvinar, "
                        + "dignissim eros nec, consectetur lorem. Suspendisse iaculis tortor id nibh consequat, eget "
                        + "efficitur enim fermentum. Sed ac mi sit amet dui cursus volutpat sed id nulla. Maecenas "
                        + "malesuada neque vitae orci efficitur bibendum. Vivamus ac nisi posuere elit egestas varius "
                        + "vitae ac lacus.")

    db.session.add(app0)
    db.session.add(app1)
    db.session.add(app2)
    db.session.commit()

    # now find these apps and set each's next to the next app
    all_apps = App.query.all()
    for i in range(len(all_apps)):
        if i+1 < len(all_apps):
            all_apps[i].next = all_apps[i+1].id
    db.session.commit()


class Guideline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=True)
    short_text = db.Column(db.String(300), nullable=False)
    external_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)


def do_log(fn):
    print("calling do_log")

    def f(a):
        print("do_log", a)
        return fn(a)
    return f


def seed_guidelines():
    print('seeding guidelines...')
    guidelines_to_seed = []
    guideline1 = Guideline(
        number=1,
        short_text="Contributes to society and to human well-being.",
        external_url="https://www.acm.org/code-of-ethics#h-1.1-contribute-to-society-and-to-human-well-being,-acknowledging-that-all-people-are-stakeholders-in-computing.",
        description=""
    )

    guidelines_to_seed.append(guideline1)
    db.session.add(guideline1)

    guideline2 = Guideline(
        number=2,
        short_text="Avoids harm.",
        external_url="https://www.acm.org/code-of-ethics#h-1.2-avoid-harm.",
        description=""
    )
    guidelines_to_seed.append(guideline2)
    db.session.add(guideline2)

    guideline3 = Guideline(
        number=3,
        short_text="Is honest and trustworthy.",
        external_url="https://www.acm.org/code-of-ethics#h-1.3-be-honest-and-trustworthy.",
        description=""
    )
    guidelines_to_seed.append(guideline3)
    db.session.add(guideline3)

    guideline4 = Guideline(
        number=4,
        short_text="Is fair and takes action not to discriminate.",
        external_url="https://www.acm.org/code-of-ethics#h-1.4-be-fair-and-take-action-not-to-discriminate.",
        description=""
    )
    guidelines_to_seed.append(guideline4)
    db.session.add(guideline4)

    guideline5 = Guideline(
        number=5,
        short_text="Respects the work required to produce new ideas, inventions, creative works, and computing artifacts.",
        external_url="https://www.acm.org/code-of-ethics#h-1.5-respect-the-work-required-to-produce-new-ideas,-inventions,-creative-works,-and-computing-artifacts.",
        description=""
    )
    guidelines_to_seed.append(guideline5)
    db.session.add(guideline5)

    guideline6 = Guideline(
        number=6,
        short_text="Respects privacy.",
        external_url="https://www.acm.org/code-of-ethics#h-1.6-respect-privacy.",
        description=""
    )
    guidelines_to_seed.append(guideline6)
    db.session.add(guideline6)

    guideline7 = Guideline(
        number=7,
        short_text="Honors confidentiality.",
        external_url="https://www.acm.org/code-of-ethics#h-1.7-honor-confidentiality.",
        description=""
    )
    guidelines_to_seed.append(guideline7)
    db.session.add(guideline7)
    print(guidelines_to_seed)

    map(do_log(db.session.add), guidelines_to_seed)
    db.session.commit()


class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('app.id'),
                       nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    justification = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

try: 
    db.create_all()
    app_reviews = App.query.all()
    if app_reviews is None or len(app_reviews) == 0:
        seed_apps()
        app_reviews = App.query.all()

    guidelines = Guideline.query.all()
    if guidelines is None or len(guidelines) == 0:
        seed_guidelines()
        guidelines = Guideline.query.all()

except sqlite3.OperationalError as issue:
    print(issue, 'occurred')


@app.route("/", strict_slashes=False)
def home():
    return render_template("home.html")


@app.route("/interaction", strict_slashes=False, methods=["POST"])
def interaction():
    data = request.form
    print(data["approved"])
    print(data["explanation"])
    print(data["next"])
    print(data)
    print(app_reviews)
    interaction = Interaction(
        app_id=data["app_id"], approved=data["approved"] == "true",
        justification=data["explanation"])
    db.session.add(interaction)
    db.session.commit()
    # Conditionally do something else at the last app to review
    return redirect(url_for("show_review", app_id=data["next"]))


@app.route("/about", strict_slashes=False)
def about():
    return render_template("about.html")


@app.route("/review/app/", strict_slashes=False)
@app.route("/review/app/<app_id>", strict_slashes=False)
def show_review(app_id="1", hash=None):
    # get_app_reviews()
    int_app_idx = int(app_id)
    return render_template("review.html",
                           app_review=app_reviews[int_app_idx-1],
                           guidelines=guidelines)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
