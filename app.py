import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
from forms import RegistrationForm, LoginForm
import json
import datetime
load_dotenv()


USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = os.getenv('MONGODB_PASSWORD')
COLLECTION_NAME = os.getenv('MONGODB_COLLECTION_NAME')


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
def all_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/my_recipes')
def my_recipes():
    if session:
        return render_template("my_recipes.html",
                               my_recipes=mongo.db.my_recipes.find())
    else:
        return ('Login first!')


@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    (request.form.to_dict())
    (request.form.to_dict())
    recipes.insert_one({
        "title": request.form['title'],
        "category_name": request.form.get('category_name'),
        "cooking_time": request.form.get('cooking_time'),
        "serves": request.form.get('serves'),
        "author": request.form.get('author'),
        "ingredients": request.form['ingredients'],
        "instructions": request.form.get('instructions')

    })
    return redirect(url_for('all_recipes'))


@app.route('/detail')
def detail():
    action = request.args.get('action')
    recipe = request.args.get('recipe')

    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    if action == 'detail':
        (the_recipe)
        return render_template("detail.html", recipe=the_recipe)
    elif action == 'edit':
        return render_template("edit_recipe.html", recipe=the_recipe)
    elif action == 'delete':
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe)})
        return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_my_recipes = mongo.db.recipes.find({"username": session['username']})
    return render_template('edit_recipe.html', recipe=the_recipe,
                           my_recipes=all_my_recipes)


@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    if request.method == 'POST':
        (request.form.to_dict())
        mongo.db.recipes.update_one(
            {"_id":  ObjectId(recipe_id)},
            {
                "$set": {
                    "title": request.form['title'],
                    "category_name": request.form.get('category_name'),
                    "cooking_time": request.form.get('cooking_time'),
                    "serves": request.form.get('serves'),
                    "author": request.form.get('author'),
                    "ingredients": request.form['ingredients'],
                    "instructions": request.form.get('instructions')
                }
            })

        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("detail.html", recipe=the_recipe)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
