from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests
from pymongo import MongoClient
from flask_pymongo import PyMongo
from models import Cupcake, c1, c2

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = "mongodb://localhost:27017/cupcakes_db"
mongo = PyMongo(app)
# client = MongoClient('localhost', 27017)
# db = client.cupcakes_db
# collection = db.cakes_list

mongo.db.insertMany([c1,c2])

@app.route('/cupcakes', methods="GET")
def get_cupcakes():
    all_cakes = mongo.db.find()
    return Response(jsonify(all_cakes), 200)

@app.route('/cupcakes/<int:id>', methods="GET")
def get_single_cake(id):
    cake = mongo.db.find({'_id': id})
    return Response(jsonify(cake), 200)

@app.route('/cupcakes/search/<string:query>', methods="GET")
def get_single_cake(query):
    cakes = mongo.db.find({'$text': {'$search': query}})
    return Response(jsonify(cakes), 200)

@app.route('/cupcakes', methods="POST")
def create_cupcake():
    cake = Cupcake(request.json)
    
    new_cake = {
        '_id': cake.id, 
        'flavor': cake.flavor,
        'size': cake.size,
        'rating': cake.rating,
        'image': cake.image
    }
    
    mongo.db.insertOne(new_cake)

    print('new cupcake:',mongo.db.find({'_id': new_cake['_id']}))
    return Response(jsonify(new_cake), 201)

@app.route('/cupcakes/update/<int:id>', methods="PATCH")
def update_cake(id):
    new_data = request.json
    mongo.db.updateOne({'_id': id}, {'$set': new_data})
    verify = mongo.db.find({'_id': id})
    return Response(jsonify(verify), 203)

@app.route('cupcakes/delete/<int:id>')
def delete_cake(id):
    mongo.db.deleteOne({'_id': id})
    verify = mongo.db.find({})
    return Response(jsonify(verify), 204)


app.run()