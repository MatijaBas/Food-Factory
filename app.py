import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import json
import datetime
load_dotenv()


USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = os.getenv('MONGODB_PASSWORD')
COLLECTION_NAME = os.getenv('MONGODB_COLLECTION_NAME')


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'food_factory'
app.config["MONGO_URI"] = 'mongodb+srv://' + USERNAME + ':' + PASSWORD + \
    '@myfirstcluster-y6kfn.mongodb.net/' + \
    COLLECTION_NAME + '?retryWrites=true&w=majority'

# print(COLLECTION_NAME)

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/all_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('/all_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
