#imports
from flask import Flask, render_template,request,redirect,url_for 
from bson import ObjectId 
from pymongo import MongoClient 
import os  

title = "Donate Direct application with Flask and MongoDB"  
heading = "Donate Direct with Flask and MongoDB"

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017") #host uri  
db = client.DonateDirect #Select the database  
DonateDirect = db.DonateDirect #Select the collection name 


# Initialize Flask app
app = Flask(__name__)


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
  
    

# ======================FIREBASE WORK =============================
# from firebase_admin import credentials, firestore, initialize_app

# import sqlalchemy
# import os
# from os.path import join, dirname
# from dotenv import load_dotenv

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# GOOGLE_APPLICATION_CREDENTIALS =  os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# # Initialize Firestore DB
# cred = credentials.Certificate('key.json')
# default_app = initialize_app(cred)
# db = firestore.client()
# vendors_ref = db.collection('vendors')


# @app.before_first_request
# def create_tables():
#     # Create tables (if they don't already exist)
#     with db.connect() as conn:
#         print(conn)
#         print(dir(conn))

# @app.route('/add', methods=['POST'])
# def create():
#     """
#         create() : Add document to Firestore collection with request body.
#         Ensure you pass a custom ID as part of json body in post request,
#         e.g. json={'id': '1', 'title': 'Write a blog post'}
#     """
#     try:
#         id = request.json['id']
#         vendors_ref.document(id).set(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"


# @app.route('/list', methods=['GET'])
# def read():
#     """
#         read() : Fetches documents from Firestore collection as JSON.
#         vendors : Return document that matches query ID.
#         all_vendors : Return all documents.
#     """
#     try:
#         # Check if ID was passed to URL query
#         vendors_id = request.args.get('id')
#         if vendors_id:
#             vendors = vendors_ref.document(vendors_id).get()
#             return jsonify(vendors.to_dict()), 200
#         else:
#             all_vendors = [doc.to_dict() for doc in vendors_ref.stream()]
#             return jsonify(all_vendors), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# @app.route('/update', methods=['POST', 'PUT'])
# def update():
#     """
#         update() : Update document in Firestore collection with request body.
#         Ensure you pass a custom ID as part of json body in post request,
#         e.g. json={'id': '1', 'title': 'Write a blog post today'}
#     """
#     try:
#         id = request.json['id']
#         vendors_ref.document(id).update(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# @app.route('/delete', methods=['GET', 'DELETE'])
# def delete():
#     """
#         delete() : Delete a document from Firestore collection.
#     """
#     try:
#         # Check for ID in URL query
#         vendors_id = request.args.get('id')
#         vendors_ref.document(vendors_id).delete()
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"



# @app.route('/webhook', methods=['POST'])
# def respond():
#     print(request.json);
#     return Response(status=200)
    

    
if __name__ == "__main__":
    app.run(debug=True)
