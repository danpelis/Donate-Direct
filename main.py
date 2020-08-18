#imports
from flask import Flask, render_template, request,redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from mongoengine import connect

from bson import ObjectId 
from pymongo import MongoClient 
import os  


app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:<MONGODB-PASS>@donate-direct.qoqxp.gcp.mongodb.net/DonateDirect?retryWrites=true&w=majority")
db = client.DonateDirect
vendors = db.vendors

def seed():
    client.drop_database('Donate-Direct')
    user1 = {'name': 'Jessica Valenzuela Redbubble', 'username': 'user', 'password': 'pass', 'charity': 'Color Of Change'}
    user2 = {'name': 'Match DNI', 'username': 'user', 'password': 'pass','charity': 'NAACP Legal Defense and Educational Fund, Inc.'}
    user3 = {'name': 'Sig Delt Fundraiser', 'username': 'user', 'password': 'pass','charity': 'The Movement for Black Lives'}
    vendors.insert_one(user1)
    vendors.insert_one(user2)
    vendors.insert_one(user3)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    """
       Function to create new users.
       """
    try:
        # Create new users
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "", 500
  

@app.route("/validate", methods=['POST'])
def validate():
    name = request.values['name']
    vendor = vendors.find({'name': name})[0]
    vendor.pop('_id')
    return jsonify({"result":vendor})
    
if __name__ == "__main__":
    seed()
    app.run(debug=True)

