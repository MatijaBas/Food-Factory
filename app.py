import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'food_factory'
app.config["MONGO_URI"] = ''

mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello..World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '3000')),
            debug=True)
