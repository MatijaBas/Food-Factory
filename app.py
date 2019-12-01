import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('MONGODB_USERNAME')
PASSWORD = os.getenv('MONGODB_PASSWORD')
COLLECTION_NAME = os.getenv('MONGODB_COLLECTION_NAME')


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'food_factory'
app.config["MONGO_URI"] = 'mongodb+srv://{USERNAME}:{PASSWORD}@myfirstcluster-y6kfn.mongodb.net/{COLLECTION_NAME}?retryWrites=true&w=majority'
print(COLLECTION_NAME)

mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello..World'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '3000')),
            debug=True)
