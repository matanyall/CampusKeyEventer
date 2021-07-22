import os
import pyqrcode # pip install pyqrcode

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
# method that takes student ID, Event ID, and Registration ID and returns unique QR code

def QR_gen(Student_ID, Event_ID):
    registration = [Student_ID, Event_ID]
    qr_code_data = "R" + registration[0] + registration[1] 
    qr_code_name = qr_code_data + ".svg"
    qr_code = pyqrcode.create(qr_code_data)
    qr_code_svg = qr_code.svg(qr_code_name, scale=8)
    register(registration, qr_code_data)
    return qr_code_svg

# TODO
# method that takes QR code and email address and sends ticket email. 
# also return registration object with info

def send_ticket(QR_image, email):
    # use aAPI to send ticket to registrant
    registration_obj = "" # object containing name and ID (for now)
    return registration_obj

# TODO
# method that makes string html map from gmplot with heatmap of events

def heatmap_gen():
    heatmap_html_string = ""
    return heatmap_html_string

# TODO
# method that takes registration object and google sheet and adds to google sheet

def register(registration_list, qr_code_data):
    sheet_name = registration_list[1] + ".txt" #Event ID is name of event sheet
    student = student_list[registration_list[0]]
    f = open(sheet_name, "a")
    f.write(qr_code_data + "; " + student["Name"] + "; " + student["Email"] + "\n")
    f.close()



    # add registrant to google sheet
    return None

# TODO
# method that takes Student ID, Event ID, and Registration ID as a list,
# and registers it in the proper event spreadsheet

def register_for_event(Name, ID, Email, Event_ID):
    make_student(Name, ID, Email)
    qr_code_svg = QR_gen(ID, Event_ID)
