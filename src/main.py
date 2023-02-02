from flask import Flask, send_file
from datetime import date
import os
app = Flask(__name__)


# this route is for the main home page. If it gets a request from "/" it will respond with index.html that
# is found in the frontend folder
@app.route("/", methods=["GET"])
def home():
    return send_file(os.getcwd() + "/frontend/index.html")

# if a request is made from "/get_date", it will respond with the current date calculated from the date.today() function
@app.route("/get_date", methods=["GET"])
def get_date():
    today = date.today()
    return "Todays date is " + str(today)


# this route is for when the index.html file requests the linked css and javascript files
@app.route("/frontend/<filename>")
def get_other_files(filename):
    return send_file(os.getcwd() + "/frontend/" + filename)


# this server will run on port 3000
app.run(port="3000")