# -*- coding: utf-8 -*-
"""
SEt the FLASK_APP as the module name
set the  FLASK_ENV=developmentfor development environment
"""



from flask import Flask,request
from Student import Student
import jsonpickle
import json

# The flask API will use the folder of this module as the root path
helloWorldSvc = Flask(__name__)

# decorator used for the index route
@helloWorldSvc.route("/")
def index():
    return "Hello World!"


@helloWorldSvc.route("/home")
def home():
    return "<h1>Welcome to home page!</h1>"


def login():
    return "<h1>Login page</h1>"

#another way of routing
helloWorldSvc.add_url_rule('/Login', 'loginRule',login,methods=["GET"])


@helloWorldSvc.route("/demo/<id>",methods=["POST","GET"])
def add(id):
    request_data = request.get_json()
    print("Data->",request_data)
    print("Path variable->",id)
    return "<h1>GET POST page</h1>"

@helloWorldSvc.route("/fetchAll",methods=["POST"])
def fetchAllStudents():
    student1 = Student(100,"John","NYC US")
    student2 = Student(101,"Ron","NYC US")
    students = [student1,student2]    
    studentJSONList = jsonpickle.encode(students,unpicklable=False)
    print("JSON List :",studentJSONList)
    return studentJSONList

@helloWorldSvc.route("/fetchStudent",methods=["POST"])
def fetchStudent():
    request_data = request.get_json()
    print("Data->",request_data)
    #Converting JSOn to Dictionary
    request_data_json= json.dumps(request_data)
    print("Data Type:",type(request_data))
    request_dataDict= jsonpickle.decode(request_data_json)    
    print("Student id:",request_data["id"])
    #Logic for fetching student from back end goes here
    student = Student(300,"Shanmu","India TN")
    studentJSON = jsonpickle.encode(student,unpicklable=False)
    print("JSON string:",studentJSON)
    return studentJSON

# Bind to all network interfaces (0.0.0.0) on port 5000
helloWorldSvc.run(host='0.0.0.0', port=5000)
