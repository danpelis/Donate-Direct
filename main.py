from flask import Flask, render_template, request, Response   
from firebase_admin import credentials, firestore, initialize_app

import sqlalchemy
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GOOGLE_APPLICATION_CREDENTIALS =  os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
vendors_ref = db.collection('vendors')


@app.before_first_request
def create_tables():
    # Create tables (if they don't already exist)
    with db.connect() as conn:
        print(conn)
        print(dir(conn))

@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        vendors_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON.
        vendors : Return document that matches query ID.
        all_vendors : Return all documents.
    """
    try:
        # Check if ID was passed to URL query
        vendors_id = request.args.get('id')
        if vendors_id:
            vendors = vendors_ref.document(vendors_id).get()
            return jsonify(vendors.to_dict()), 200
        else:
            all_vendors = [doc.to_dict() for doc in vendors_ref.stream()]
            return jsonify(all_vendors), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        vendors_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection.
    """
    try:
        # Check for ID in URL query
        vendors_id = request.args.get('id')
        vendors_ref.document(vendors_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
    

    
if __name__ == "__main__":
    app.run(debug=True)
