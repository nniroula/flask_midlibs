from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route("/flask")
# def testing_flask_setup():
#     return "Your Flask is working properly."

# get form for user input
@app.route("/user-form")
def get_form():
    return render_template("form1.html")

@app.route("/story")
def get_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("story.html", place=place, noun=noun, verb=verb, adjective = adjective, plural_noun = plural_noun)