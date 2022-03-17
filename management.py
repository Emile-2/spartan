import json
from spartan import Spartan
import main
from flask import Flask, request, jsonify


# def sparta_dicts():
#     global sparta_dict
#     sparta_dict = {}
#     return sparta_dict

def sparta_request():
    sparta_data = request.data
    return sparta_data

def add_spartan(sparta_data):

    # sparta_data = request.json  #
    sparta_id = sparta_data['spartan_id']
    first_name = sparta_data['first_name']
    last_name = sparta_data['last_name']
    birth_year = sparta_data['birth_year']
    birth_month = sparta_data['birth_month']
    birth_day = sparta_data['birth_day']
    course = sparta_data['course']
    stream = sparta_data['stream']

    # call the method that will create the employee record

    trainee_obj = Spartan(sparta_id, first_name, last_name, birth_year, birth_month, birth_day, course, stream)
    trainee_obj.print_all()
    # return f"The employee ({sparta_id}: {first_name} {last_name} {birth_year} {birth_month} {birth_day} {course} {stream})"

    sparta_dict[sparta_id] = trainee_obj
    print('--------------sparta dict of objects-------')
    print(sparta_dict)
    print('--------------individual trainee obj-------')
    print(trainee_obj)

    json_save()

    return "added"

def read_employee_id():
    id_str = input("Please Enter the Employee ID:")
    id_str = id_str.strip()

    if id_str.isdigit():
        id = int(id_str)
        if id > 0:
            return id
        else:
            print("Error, The Employee ID should be positive number")
    else:
        print("Error, The Employee ID should be a number")


def read_name(text, name):
    name = name.strip()

    if len(name) >= 2:
        return name
    else:
        return (f"Error, The Employee {text} Name should be at least 2 Characters\n")


def read_text(text, course_str):
    # course = course_str.strip()

    if len(course_str) >= 2:
        return course_str
    else:
        return f"Error, The {text} should be at least 2 Characters\n"

def read_year(year_str):

    # if year_str.isdigit():
    year = int(year_str)
    if (year >= 1900) and (year <= 2004):
        return year
    else:
        print("Error, The Employee Birth Year should be between 1900 and 2004")
    # else:
    #     print("Error, The Employee Birth Year should be a number")


def read_month(month_str):
    # month_str = month_str.strip()

    # if month_str.isdigit():
    month = int(month_str)
    if (month >= 1) and (month <= 12):
        return month
    else:
        print("Error, The Employee Birth Month should be between 1 and 12")
    # else:
    #     print("Error, The Employee Birth Month should be a number")


def read_day(day_str):
    # day_str = day_str.strip()

    # if day_str.isdigit():
    day = int(day_str)
    if (day >= 1) and (day <= 31):
        return day
    else:
        print("Error, The Employee Birth Day should be between 1 and 31")
    # else:
    #     print("Error, The Employee Birth Day should be a number")


def json_load(sparta_dict_v):
    global sparta_dict
    with open("data.json", "r") as jsonload:
        return_spartan = json.load(jsonload)

    for spartan_id_key in return_spartan:
        return_spartan[spartan_id_key]
        n_emp_id = return_spartan[spartan_id_key]["spartan_id"]
        n_f_name = return_spartan[spartan_id_key]["first_name"]
        n_l_name = return_spartan[spartan_id_key]["last_name"]
        n_y_ob = return_spartan[spartan_id_key]["birth_year"]
        n_m_ob = return_spartan[spartan_id_key]["birth_month"]
        n_d_ob = return_spartan[spartan_id_key]["birth_day"]
        n_course = return_spartan[spartan_id_key]["course"]
        n_stream = return_spartan[spartan_id_key]["stream"]

        new = Spartan(n_emp_id, n_f_name,n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream )
        sparta_dict_v[spartan_id_key] = new
        print("___this is new_____")
        print(sparta_dict_v)

def json_save(sparta_dict_v):
    global sparta_dict
    # want to get the keys from the dictionary of objects, and add those object values to a dictionary of dictionary and add that to the json file
    temp_dict_of_dict = {}  # creating an empty dictionary to store the employee dictionary as visual data/ not objects

    for sparta_id in sparta_dict_v:  # iterating through the keys in the sparta dictionary
        multiple_sparta_obj = sparta_dict_v[
            sparta_id]  # creating a variable which contains the sparta_objects in the dictionary/ at the sparta id location
        sparta_dict_json = multiple_sparta_obj.__dict__  # creating a variable which opens the sparta_object_dict and visualises it as a dictionary
        temp_dict_of_dict[
            sparta_id] = sparta_dict_json  # using the temp dict of dict to store the employee_obj_dict at the respective employee id key

    with open("data.json",
              "w") as sparta_json_dict_of_dict:  # opening the json file in write mode, overides the data on there already
        json.dump(temp_dict_of_dict, sparta_json_dict_of_dict,
                  indent=4)  # dumping the dictionary of dicts in the json file and format
#
# if __name__ == "__main__":
#     sparta_dict = {}
