import json
from spartan import Spartan
from flask import request

# def sparta_request():
#     sparta_data = request.data
#     return sparta_data

def add_spartan(sparta_dict_v):
    global v_dict

    sparta_data = request.json
    try:
        sparta_id = read_sparta_id(sparta_data['spartan_id'])
    except Exception:
        return "Error, Spartan ID must be a positive number"

    if sparta_id == False:
        return "Error, Spartan ID must be a positive number"

    if str(sparta_id) in sparta_dict_v.keys():
        return "This ID is already in our records"

    first_name_v = read_name(sparta_data['first_name'])
    if first_name_v == False:
        return "First name must be more than one character"

    last_name = read_name(sparta_data['last_name'])
    if last_name == False:
        return "Last Name must be more than one character"

    birth_year = read_year(sparta_data['birth_year'])
    if birth_year == False:
        return "Birth year must be a digit and between 1900-2000"

    birth_month = read_month(sparta_data['birth_month'])
    if birth_month == False:
        return "Birth month must be a digit and between 1-12"

    birth_day = read_day(sparta_data['birth_day'])
    if birth_day == False:
        return "Birth day must be a digit and between 1-31"

    course = read_text('Course', sparta_data['course'])
    if course == False:
        return "Course must be more than 1 character"

    stream = read_text("Stream", sparta_data['stream'])
    if stream == False:
        return "Stream must be more than 1 character"

    # call the method that will create the employee record

    trainee_obj = Spartan(sparta_id, first_name_v, last_name,
                          birth_year, birth_month, birth_day,
                          course, stream)

    # trainee_obj.print_all()
    sparta_dict_v[sparta_id] = trainee_obj

    # json_save(v_dict)
    return f"Spartan ID: {trainee_obj.get_spartan_id()}'s details have been successfully added to the system"

def read_sparta_id(spartan_id):
    try:
        id_str = str(spartan_id)
        id_str = id_str.strip()

        if id_str.isdigit():
            id_str = int(id_str)
            if id_str > 0:
                return spartan_id
            else:
                return False
        else:
            return False
    except Exception as ex:

        return False

def list_prep(): pass


def read_name(name_str):
    name_str = str(name_str)
    name = name_str.strip()
    print("------ THIS IS readname---------")

    print(type(name))

    if len(name_str) >= 2:
        return name_str
    else:
        return False


def read_text(text, course_str):
    course_str = str(course_str)
    course = course_str.strip()

    if len(str(course)) >= 2:
        return course_str
    else:
        return False

def read_year(year_str):
    year_str = str(year_str)
    try:
        if year_str.isdigit():
            year = int(year_str.strip())
        if (year >= 1900) and (year <= 2004):
            return year
        else:
            return False
    except Exception as ex:
        return False


def read_month(month_str):

    month_str = str(month_str)
    try:
        if month_str.isdigit():
            month = int(month_str.strip())
        if (month >= 1) and (month <= 12):
            return month
        else:
            return False
    except Exception as ex:
        return False


def read_day(day_str):
    day_str = str(day_str)
    try:
        if day_str.isdigit():
            day = int(day_str.strip())
        if (day >= 1) and (day <= 31):
            return day
        else:
            return False
    except Exception:
        return False


def json_load(sparta_dict_v):
    global sparta_dict

    try:
        with open("data.json", "r") as jsonload:
            return_spartan = json.load(jsonload)

    except Exception as ex:
        return ("Records empty")

    for spartan_id_key in return_spartan:

        n_emp_id = return_spartan[spartan_id_key]["spartan_id"]
        n_f_name = return_spartan[spartan_id_key]["first_name"]
        n_l_name = return_spartan[spartan_id_key]["last_name"]
        n_y_ob = return_spartan[spartan_id_key]["birth_year"]
        n_m_ob = return_spartan[spartan_id_key]["birth_month"]
        n_d_ob = return_spartan[spartan_id_key]["birth_day"]
        n_course = return_spartan[spartan_id_key]["course"]
        n_stream = return_spartan[spartan_id_key]["stream"]

        new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream )
        sparta_dict_v[spartan_id_key] = new


def json_save(sparta_dict_v):
    global sparta_dict
    # want to get the keys from the dictionary of objects, and add those object values to a dictionary of dictionary and add that to the json file
    temp_dict_of_dict = {}  # creating an empty dictionary to store the spartan dictionary as visual data/ not objects

    for sparta_id in sparta_dict_v:  # iterating through the keys in the sparta dictionary
        multiple_sparta_obj = sparta_dict_v[sparta_id]  # creating a variable which contains the sparta_objects in the dictionary/ at the sparta id location

        sparta_dict_json = multiple_sparta_obj.__dict__  # creating a variable which opens the sparta_object_dict and visualises it as a dictionary

        temp_dict_of_dict[sparta_id] = sparta_dict_json  # using the temp dict of dict to store the sparta employee dict of info at the respective employee id key
    try:

        with open("data.json", "w") as sparta_json_dict_of_dict:  # opening the json file in write mode, overides the data on there already
            json.dump(temp_dict_of_dict, sparta_json_dict_of_dict,indent=4)  # dumping the dictionary of dicts in the json file and format

    except Exception:
        return "File not found"


# def spartan_obj_list():
#
#     temp_dict = {}
#     with open("data.json", "r") as jsonload:
#         return_spartan = json.load(jsonload)
#
#     for spartan_id_key in return_spartan:
#         n_emp_id = return_spartan[spartan_id_key]["spartan_id"]
#         n_f_name = return_spartan[spartan_id_key]["first_name"]
#         n_l_name = return_spartan[spartan_id_key]["last_name"]
#         n_y_ob = return_spartan[spartan_id_key]["birth_year"]
#         n_m_ob = return_spartan[spartan_id_key]["birth_month"]
#         n_d_ob = return_spartan[spartan_id_key]["birth_day"]
#         n_course = return_spartan[spartan_id_key]["course"]
#         n_stream = return_spartan[spartan_id_key]["stream"]
#
#         new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)
#         temp_dict[spartan_id_key] = new
#
#         return temp_dict[spartan_id_key].print_all()

def spartan_id_get(sparta_id):

    with open("data.json", "r") as jsonload:
        return_spartan = json.load(jsonload)

    temp_dict = {}
    if sparta_id in return_spartan.keys():
        n_emp_id = return_spartan[sparta_id]["spartan_id"]
        n_f_name = return_spartan[sparta_id]["first_name"]
        n_l_name = return_spartan[sparta_id]["last_name"]
        n_y_ob = return_spartan[sparta_id]["birth_year"]
        n_m_ob = return_spartan[sparta_id]["birth_month"]
        n_d_ob = return_spartan[sparta_id]["birth_day"]
        n_course = return_spartan[sparta_id]["course"]
        n_stream = return_spartan[sparta_id]["stream"]

        new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)
        temp_dict[sparta_id] = new
        return new.print_all()
    else:
        return "This ID is not in our records"







