from flask import Flask, render_template, current_app, g, request, jsonify , url_for , redirect
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson import json_util, ObjectId
from flask.json.provider import DefaultJSONProvider
from datetime import datetime, timedelta
import configparser
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://almashooq:Qazw2003@cs390project.07mjq.mongodb.net/?retryWrites=true&w=majority&ssl=true&appName=CSARCS"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

db = client["CSARCS"] 


@app.route("/", methods=["GET"])
def Main():
    return render_template("Main.html")

@app.route("/signup", methods=["GET", "POST"])
def Sign_Up():
    if request.method == "GET":
        return render_template("Sign_Up.html")
    elif request.method == "POST":
        try:
            person_data = request.json
            print(person_data)
            db.People.insert_one(person_data)
            return redirect(url_for("Login"))
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "GET":
        return render_template("Login.html")
    elif request.method == "POST":
        try:
            person_data = request.json
            print("Received data:", person_data)
            if not person_data:
                return jsonify({"success": False, "error": "No data received"}), 400
            
            email = person_data.get("email")
            password = person_data.get("password")
            
            user = db.People.find_one({"email": email})
            if not user:
                return jsonify({"success": False, "error": "User not found"}), 404
            
            role = user.get('role')
            if not role:
                return jsonify({"success": False, "error": "Role not defined for user"}), 400

            role_routes = {
                "junior": "junior",
                "senior": "senior",
                "faculty": "faculty"
            }
            redirect_route = role_routes.get(role.lower())
            print(f"User role: {role}")
            print(f"Redirecting to: {redirect_route}")

            if not redirect_route:
                return jsonify({"success": False, "error": f"Invalid role: {role}"}), 400

            return redirect(url_for(redirect_route))
        
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 500



@app.route("/junior", methods=["GET"])
def junior():
    return render_template("JuniorLandpage.html")

@app.route("/senior", methods=["GET"])
def senior():
    print("rendring")
    return render_template("SeniorLandpage.html")

@app.route("/faculty", methods=["GET"])
def faculty():
    return render_template("Faculty_Dashboard.html")

@app.route("/room", methods=["GET"])
def Access_Room():
    return render_template("Access_Room.html")

if __name__ == "__main__":
    app.run()
