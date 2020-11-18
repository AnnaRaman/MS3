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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "difficulty": request.form.get("difficulty"),
            "name": request.form.get("name"),
            "description": request.form.get("description")
        }
        mongo.db.recipe.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for("get_recipe"))

    difficulty = mongo.db.difficulty.find().sort("difficulty", 1)
    return render_template("add_recipe.html", difficulty=difficulty)

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "difficulty": request.form.get("difficulty"),
            "name": request.form.get("name"),
            "description": request.form.get("description")
        }
        mongo.db.recipe.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated!")

    recipe = mongo.db.recipe.find_one({"_id":ObjectId()})
    difficulty = mongo.db.difficulty.find().sort("difficulty", 1)
    return render_template("edit_recipe.html", recipe=recipe, difficulty=difficulty)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({"_id": ObjectId()})
    flash("Recipe Successfully Deleted!")
    return redirect(url_for("get_recipe"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)