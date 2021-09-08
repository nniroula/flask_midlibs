from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-no-secret-key"
debug = DebugToolbarExtension(app)

# @app.route("/flask")
# def testing_flask_setup():
#     return "Your Flask is working properly."

# get form for user input
@app.route("/user-form")
def get_form():
    "This shows form to a user "
    # get prompting words from a Story class
    prompting_words = story.prompts
    return render_template("form1.html", prompting_words = prompting_words)


@app.route("/story")
def get_story():
    """ retuns the story after user gives inputs """
    # place = request.args["place"]  # these are for individual forms, but we are given a story
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args["plural_noun"]
    generate_story = story.generate(request.args)
    # return render_template("story.html", place=place, noun=noun, verb=verb, adjective = adjective, plural_noun = plural_noun)
    return render_template("story.html", generate_story = generate_story)

@app.route("/")
def get_main_form():
    """ Shows dropdown list of fun stories. """
    return render_template("home_page.html")

@app.route("/Math")
def get_math_story():
    noun = request.args["noun"]
    verb = request.args["verb"]
    return render_template("math_html.html", noun = noun, verb = verb)
