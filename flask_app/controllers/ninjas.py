# session would be added to the end of the following line if we were using it in this file
from flask import render_template, redirect, request
from flask_app import app
# import the class from friend.py
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninja/new")
def display_create_ninja():
    return render_template("create_ninja.html", dojos = Dojo.get_all_dojos())

@app.route("/ninja/new", methods = ['POST'])
def create_ninja():
    data = {
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Ninja.create(data)
    # To redirect to "/dojos/<int:id>", we do not have just the id coming into this function. The id that we are referring to is the id associated with a dojo, so we can save the dojo id from the request form in a variable and use an f string to put that in the redirect url string.
    dojo_id = request.form["dojo_id"]
    return redirect(f"/dojos/{dojo_id}")