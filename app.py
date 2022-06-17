from flask import Flask, render_template, jsonify, request, session, Response, redirect
from flask_cors import CORS
import requests
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('localhost', 27017)
db = client.cupcakes_db
collection = db.cakes_list

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()