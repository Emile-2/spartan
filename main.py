from spartan import *
from flask import Flask, request, jsonify
import json
import management

flask_object = Flask(__name__)  # telling py i want to create a new server

@flask_object.route('/', methods=["GET"])  # when user asks for nothing (/), run this method
def home_page():
    return """
    Welcome to Emile's Server
    Use the following API's to navigate
    After http://127.0.0.1:5000/
    Remove Spartan from records: /spartan/remove?id=sparta_id
    Add Spartan to records: /spartan_add
    View specific Spartan record by ID: /spartan/'enter spartan id here'   
    """


@flask_object.route('/spartan_add', methods=['POST'])  # allows user to add sparta data by passing json file
def add_spartan_api():

    sparta_data = request.json

    return management.adding_spartan(sparta_data)


# http://127.0.0.1:5000//spartan/<spartan_id> get certain employee data, return error message if id doesnt exists in system, return as string
@flask_object.route('/spartan/<spartan_id>', methods=["GET"])
def sparta_id_getter(spartan_id):

    return management.spartan_id_get(spartan_id)


# #http://127.0.0.1:5000/spartan/remove?id=sparta_id   This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string
@flask_object.route('/spartan/remove', methods=['POST'])
def remove(): # can this be done in the <> method

    id_to_remove = request.args.get("id")
    return management.remove_spartan(id_to_remove)

@flask_object.route('/spartan', methods=["GET"])
def list_all():

    return jsonify(management.list_spartans())

if __name__ == "__main__":

    # sparta_dict = {}


    flask_object.run(debug=True)  # dont use debug true when pushing to server