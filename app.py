from flask import Flask, render_template, jsonify, request, session, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()