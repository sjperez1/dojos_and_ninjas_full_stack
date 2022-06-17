# session would be added to the end of the following line if we were using it in this file
from flask import render_template, redirect, request
from flask_app import app
# import the class from friend.py
from flask_app.models.dojo import Dojo

@app.route("/")
@app.route("/dojos")
def display_create_dojos():
    return render_template("new_show_dojos.html", dojos = Dojo.get_all_dojos())

@app.route("/dojos", methods = ['POST'])
def create_dojos():
    data = {
        "name" : request.form["name"]
    }

    Dojo.create(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def display_dojo_ninjas(id):
    data = {
        "id" : id
    }
    return render_template("show_ninjas.html", ninjas = Dojo.get_all_ninjas(data))