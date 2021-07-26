import os
import pyqrcode # pip install pyqrcode
from . import send_email
from . import heat_map
from flask_files.app import test_app
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# app = test_app()
# app.run(host="localhost", port=5000)


student_list = {}


# generates a student dictionary of name, ID, and email and adds it to student_list

def make_student(Name, ID, Email):
    student = {
        "Name": Name,
        "Student ID": ID,
        "Email": Email 
    }
    student_list[ID] = student

# TODO 
# method that takes student ID, Event ID, and Registration ID and returns unique QR code file name

def QR_gen(Student_ID, Event_ID):
    registration = [Student_ID, Event_ID]
    qr_code_data = "R" + registration[0] + registration[1] 
    qr_code_name = qr_code_data + "qr.svg"
    qr_code = pyqrcode.create(qr_code_data)
    qr_code_svg = qr_code.svg(qr_code_name, scale=8)
    register(registration, qr_code_data)
    send_ticket(student_list[Student_ID], qr_code_name, Event_ID)
    return qr_code_name

def QR_gen_code_only(Student_ID, Event_ID):
    registration = [Student_ID, Event_ID]
    qr_code_data = "R" + registration[0] + registration[1] 
    qr_code_name = qr_code_data + "qr.svg"
    qr_code = pyqrcode.create(qr_code_data)
    qr_code_svg = qr_code.svg(qr_code_name, scale=8)
    register(registration, qr_code_data)
    return qr_code_name


# TODO
# method that takes QR code and email address and sends ticket email. 
# also return registration object with info

def send_ticket(student_dict, qr_code_image, Event_ID):
    # use Gmail API to send ticket to registrant
    send_email.send_email_with_ticket(student_dict, qr_code_image, Event_ID)

# TODO
# method that makes string html map from gmplot with heatmap of events

def heatmap_gen():
    heat_map.make_heat_map()

# TODO
# method that takes registration object and google sheet and adds to google sheet

def register(registration_list, qr_code_data):
    sheet_name = registration_list[1] + ".txt" #Event ID is name of event sheet
    student = student_list[registration_list[0]]
    f = open(sheet_name, "a")
    f.write(qr_code_data + "; " + student["Name"] + "; " + student["Email"] + "\n")
    f.close()
    return None

# TODO
# method that takes Student ID, Event ID, and Registration ID as a list,
# and registers it in the proper event spreadsheet

def register_for_event(Name, ID, Email, Event_ID):
    make_student(Name, ID, Email)
    qr_code_svg = QR_gen(ID, Event_ID)

def register_for_event_qr_only(Name, ID, Email, Event_ID):
    make_student(Name, ID, Email)
    qr_code_svg_only_name = QR_gen_code_only(ID, Event_ID)
    # print(qr_code_svg_only_name)
    return qr_code_svg_only_name

def start_flask():
    app = test_app()
    app.run(host="localhost", port=5000)