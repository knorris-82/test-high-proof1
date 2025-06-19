from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/whiskeyRecommend", methods=["GET", "POST"])
def whiskeyRecommend():
    whiskey = request.form.get("whiskey_name")
    input_data = json.dumps({"whiskey_name": whiskey})
    url = "https://test-high-proof1-307fba3a69d9.herokuapp.com/api"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=input_data, headers=headers)
        response.raise_for_status()
        results_json = response.json()
    except Exception as e:
        print(f"API error: {e}")
        results_json = {"error": "Failed to retrieve recommendations."}

    return render_template("index.html", results=results_json)

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    whiskey_name = data.get("whiskey_name", "")

    # Dummy logic - replace with model predictions as needed
    recommendations = [
        f"Try {whiskey_name} Reserve",
        f"{whiskey_name} Select Edition",
        f"{whiskey_name} Small Batch"
    ]

    return jsonify(recommendations)

"""from application import app
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
    url = "https://test-high-proof1-307fba3a69d9.herokuapp.com/api"

    #now we do our post to the url
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=input_data, headers=headers)

    results_json = response.json() #parsing the json response
    print("Response JSON from backend")
    print(results_json)

    return render_template("index.html", results=results_json)"""