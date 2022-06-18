from flask import Flask, render_template, jsonify, request, session, Response, redirect
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
    return Response(all_cakes, 200)

@app.route('/cupcakes/<int:id>', methods="GET")
def get_single_cake(id):
    cake = collection.find({'_id': id})
    return Response(cake, 200)

@app.route('/cupcakes', methods="POST")
def create_cupcake():
    new_cake = Cupcake(request.json)
    collection.insertOne(new_cake)

    print('new cupcake:',collection.find({'_id': new_cake['_id']}))
    return Response(new_cake, 200)


app.run()