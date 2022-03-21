import json
from spartan import Spartan


def read_sparta_id(spartan_id):
    try:
        id_str = str(spartan_id)
        if id_str.isdigit():
            id_str = int(id_str.strip())
            if id_str > 0:
                return spartan_id
            else:
                return False
        else:
            return False
    except Exception as ex:

        return False


def read_name(name_str):
    name_str = str(name_str)
    if len(name_str.strip()) >= 2:
        return name_str
    else:
        return False


def read_text(course_str):
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

        new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)
        sparta_dict_v[spartan_id_key] = new


# def json_save(sparta_dict_v):
#     global sparta_dict
#
#     temp_dict_of_dict = {}
#
#     for sparta_id in sparta_dict_v:
#         multiple_sparta_obj = sparta_dict_v[sparta_id]
#         sparta_dict_json = multiple_sparta_obj.__dict__
#         temp_dict_of_dict[sparta_id] = sparta_dict_json
#     try:
#
#         with open("data.json", "w") as sparta_json_dict_of_dict:
#             json.dump(temp_dict_of_dict, sparta_json_dict_of_dict, indent=4)
#     except Exception:
#         return "File not found"


def spartan_id_get(sparta_id):
    try:
        with open("data.json", "r") as jsonload:
            return_spartan = json.load(jsonload)
    except Exception:
        return "File not found"

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


def adding_spartan(sparta_data):
    global sparta_dict

    try:
        with open("data.json", "r+") as jsonload:  ##loading part
            return_spartan = json.load(jsonload)

        for spartan_id_key in return_spartan:
            n_emp_id = return_spartan[spartan_id_key]["spartan_id"]  ##### instance
            n_f_name = return_spartan[spartan_id_key]["first_name"]
            n_l_name = return_spartan[spartan_id_key]["last_name"]
            n_y_ob = return_spartan[spartan_id_key]["birth_year"]
            n_m_ob = return_spartan[spartan_id_key]["birth_month"]
            n_d_ob = return_spartan[spartan_id_key]["birth_day"]
            n_course = return_spartan[spartan_id_key]["course"]
            n_stream = return_spartan[spartan_id_key]["stream"]

            new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)

            sparta_dict[spartan_id_key] = new
    except Exception:
        pass

    try:
        sparta_id = read_sparta_id(sparta_data['spartan_id'])
    except Exception:
        return "Error, Spartan ID must be a positive number"

    if sparta_id == False:
        return "Error, Spartan ID must be a positive number"

    if sparta_id in sparta_dict:
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

    course = read_text(sparta_data['course'])
    if course == False:
        return "Course must be more than 1 character"

    stream = read_text(sparta_data['stream'])
    if stream == False:
        return "Stream must be more than 1 character"

    # call the method that will create the employee record
    if str(sparta_id) not in sparta_dict.keys():

        trainee_obj = Spartan(sparta_id, first_name_v, last_name,
                              birth_year, birth_month, birth_day,
                              course, stream)

        sparta_dict[sparta_id] = trainee_obj

        temp_dict_of_dict = {}

        for sparta_id in sparta_dict:
            multiple_sparta_obj = sparta_dict[sparta_id]

            sparta_dict_json = multiple_sparta_obj.__dict__

            temp_dict_of_dict[sparta_id] = sparta_dict_json
        try:

            with open("data.json",
                      "w") as sparta_json_dict_of_dict:  # opening the json file in write mode, overides the data on there already
                json.dump(temp_dict_of_dict, sparta_json_dict_of_dict,
                          indent=4)  # dumping the dictionary of dicts in the json file and format

        except Exception:
            return "File not found"

        return f"Spartan ID: {trainee_obj.get_spartan_id()}'s details have been successfully added to the system"


def list_spartans():
    global sparta_dict

    try:
        with open("data.json", "r") as jsonload:
            return_spartan = json.load(jsonload)

        all_spartans = []

        for spartan_id_key in return_spartan:
            n_emp_id = return_spartan[spartan_id_key]["spartan_id"]
            n_f_name = return_spartan[spartan_id_key]["first_name"]
            n_l_name = return_spartan[spartan_id_key]["last_name"]
            n_y_ob = return_spartan[spartan_id_key]["birth_year"]
            n_m_ob = return_spartan[spartan_id_key]["birth_month"]
            n_d_ob = return_spartan[spartan_id_key]["birth_day"]
            n_course = return_spartan[spartan_id_key]["course"]
            n_stream = return_spartan[spartan_id_key]["stream"]

            new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)
            sparta_dict = new

            all_spartans.append(new.__dict__)

        return all_spartans

    except Exception as ex:
        return ("Records empty")


def remove_spartan(id_to_remove):
    global sparta_dict

    try:
        with open("data.json", "r+") as jsonload:  ##loading part
            return_spartan = json.load(jsonload)

        for spartan_id_key in return_spartan:
            n_emp_id = return_spartan[spartan_id_key]["spartan_id"]  ##### instance
            n_f_name = return_spartan[spartan_id_key]["first_name"]
            n_l_name = return_spartan[spartan_id_key]["last_name"]
            n_y_ob = return_spartan[spartan_id_key]["birth_year"]
            n_m_ob = return_spartan[spartan_id_key]["birth_month"]
            n_d_ob = return_spartan[spartan_id_key]["birth_day"]
            n_course = return_spartan[spartan_id_key]["course"]
            n_stream = return_spartan[spartan_id_key]["stream"]

            new = Spartan(n_emp_id, n_f_name, n_l_name, n_y_ob, n_m_ob, n_d_ob, n_course, n_stream)

            sparta_dict[spartan_id_key] = new
    except Exception:
        pass

    try:
        del sparta_dict[id_to_remove]

    except Exception as ex:
        return f"ID: {id_to_remove} does not exist"

    temp_dict_of_dict = {}

    for sparta_id in sparta_dict:
        multiple_sparta_obj = sparta_dict[sparta_id]

        sparta_dict_json = multiple_sparta_obj.__dict__

        temp_dict_of_dict[sparta_id] = sparta_dict_json
    try:
        with open("data.json",
                  "w") as sparta_json_dict_of_dict:
            json.dump(temp_dict_of_dict, sparta_json_dict_of_dict,
                      indent=4)
    except Exception:
        return "File not found"

    return f"User would like to remove: {id_to_remove}"


sparta_dict = {}
