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
    


    """

@flask_object.route('/spartan_add', methods=['POST'])  # allows user to add sparta data by passing json file
def add_spartan_api():

    management.json_load(v_dict)

    adding = management.add_spartan(v_dict)

    management.json_save(v_dict)

    return adding

    # trainee_obj = Spartan(sparta_id, first_name_v, last_name, birth_year, birth_month, birth_day, course, stream)
    # trainee_obj.print_all()
    #
    # sparta_dict[sparta_id] = trainee_obj



# http://127.0.0.1:5000//spartan/<spartan_id> get certain employee data, return error message if id doesnt exists in system, return as string
@flask_object.route('/spartan/<spartan_id>', methods=["GET"])
def sparta_id_getter(spartan_id):
    # Check the database, read from a file, etc
    # from v_dict check the spartan_id key, if exists, return that data to sender

    management.json_load(v_dict)

    #obj_data[id_to_check] should be an object that i can use the class functions on but its not
    id_to_check = v_dict[spartan_id]

    obj_data = id_to_check

# #http://127.0.0.1:5000/spartan/remove?id=sparta_id   This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string
@flask_object.route('/spartan/remove', methods=['POST'])
def remove(): # can this be done in the <> method
    management.json_load(v_dict)

    id_to_remove = request.args.get("id")
    try:
        del v_dict[id_to_remove]
    except Exception as ex:
        return f"ID: {id_to_remove} does not exist"

    management.json_save(v_dict)

    return f"User would like to remove: {id_to_remove}"




@flask_object.route('/spartan', methods=["GET"])
def list_all():

    return "User would like to list the Spartans as one JSON object"


if __name__ == "__main__":
    sparta_dict = {}
    v_dict = sparta_dict


    flask_object.run(debug=True)  # dont use debug true when pushing to server