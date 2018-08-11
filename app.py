from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars1

# import pymongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    # listings = mongo.db.listings.find_one()
    listings = mongo.db.listings.find()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():

    # conn = 'mongodb://localhost:27017'
    # client = pymongo.MongoClient(conn)
    # db = client.mars_db
    # db.listings.drop()
    # collection = db.listings

    listings = mongo.db.listings
    listings_data = scrape_mars1.scrape()
    mongo.db.listings.drop()
    mongo.db.listings.insert_many(listings_data)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
