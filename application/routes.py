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
    whiskey = request.form.get("whiskey_name")
    results_json = {
        "recommendations": ["Mock Whisky A", "Mock Whisky B", "Mock Whisky C"]
    }
    return render_template("index.html", results=results_json)
