from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests
from pymongo import MongoClient
from models import Cupcake, c1, c2

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
db = client.cupcakes_db
collection = db.cakes_list

collection.insertMany([c1,c2])

@app.route('/cupcakes', methods="GET")
def get_cupcakes():
    all_cakes = collection.find({})
    return Response(jsonify(all_cakes), 200)

@app.route('/cupcakes/<int:id>', methods="GET")
def get_single_cake(id):
    cake = collection.find({'_id': id})
    return Response(jsonify(cake), 200)

@app.route('/cupcakes/search/<string:query>', methods="GET")
def get_single_cake(query):
    cakes = collection.find({'$text': {'$search': query}})
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
    
    collection.insertOne(new_cake)

    print('new cupcake:',collection.find({'_id': new_cake['_id']}))
    return Response(jsonify(new_cake), 201)

@app.route('/cupcakes/update/<int:id>', methods="PATCH")
def update_cake(id):
    new_data = request.json
    collection.updateOne({'_id': id}, new_data)
    verify = collection.find({'_id': id})
    return Response(jsonify(verify), 203)

@app.route('cupcakes/delete/<int:id>')
def delete_cake(id):
    collection.deleteOne({'_id': id})
    verify = collection.find({})
    return Response(jsonify(verify), 204)


app.run()