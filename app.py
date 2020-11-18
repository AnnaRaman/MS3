import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipe")
def get_recipe():
    recipe = list(mongo.db.recipe.find())
    return render_template("recipes.html", recipe=recipe)


@app.route("/add_recipe")
def add_recipe():
    difficulty = mongo.db.difficulty.find().sort("difficulty", 1)
    return render_template("add_recipe.html", difficulty=difficulty)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)