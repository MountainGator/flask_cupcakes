from flask import Flask, jsonify, request, Response
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from models import Cupcake, c1, c2
import json
from bson.json_util import dumps




app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
db = client.cupcakes
collection = db.list


# collection.insert_many([c1.get_json(),c2.get_json()])

@app.route('/cupcakes', methods=["GET"])
def get_cupcakes():
    json_docs = []
    all_cakes = collection.find({})
    for doc in all_cakes:
        # json_doc = dumps(doc)
        json_docs.append(doc)
    print('json docs:',json_docs)
    return ({'data': json_docs})

@app.route('/cupcakes/<int:id>', methods=["GET"])
def get_single_cake(id):
    cake = collection.find({'_id': id})
    return Response(jsonify(cake), 200)

@app.route('/cupcakes/search/<string:query>', methods=["GET"])
def query_cake(query):
    cakes = collection.find({'$text': {'$search': query}})
    return Response(jsonify(cakes), 200)

@app.route('/cupcakes', methods=["POST"])
def create_cupcake():
    cake = Cupcake(request.json)
    
    collection.insert_one(cake.get_json())

    print('new cupcake:',collection.find({'_id': cake['_id']}))
    return Response(jsonify(cake.get_json()), 201)

@app.route('/cupcakes/update/<int:id>', methods=["PATCH"])
def update_cake(id):
    new_data = request.json
    collection.update_one({'_id': id}, {'$set': new_data})
    verify = collection.find({'_id': id})
    print('db response to patch:', verify)
    return Response(jsonify(verify), 203)

@app.route('/cupcakes/delete/<int:id>', methods=["DELETE"])
def delete_cake(id):
    collection.delete_one({'_id': id})
    verify = collection.find({})
    return Response(jsonify(verify), 204)
