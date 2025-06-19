from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#decorator that will access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/whiskeyRecommend", methods=["GET", "POST"])
def whiskeyRecommend():
    #let's get the form input
    whiskey = request.form.get("whiskey_name")

    #converting the data to json
    input_data = json.dumps({"whiskey_name": whiskey})

    #url to send the data to our model
    url = "http://localhost:5000/api"

    #now we do our post to the url
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=input_data, headers=headers)

    results_json = response.json() #parsing the json response
    print("Response JSON from backend")
    print(results_json)

    return render_template("index.html", results=results_json)
