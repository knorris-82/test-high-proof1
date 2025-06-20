from application import app
from flask import render_template, request
import pandas as pd
import numpy as np

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/whiskeyRecommend", methods=["GET", "POST"])
def whiskeyRecommend():
    whiskey = request.form.get("whiskey_name")

    # Call local function to get recommendations
    results = get_recommendations(whiskey)

    return render_template("index.html", results=results)

def get_recommendations(whiskey_name):
    """
    Replace this dummy function with your actual recommendation logic.
    For now, it returns 3 placeholder recommendations.
    """
    # Example: match string, use dataset, or ML model (as you see fit)
    if not whiskey_name:
        return {"recommendations": ["Please enter a whiskey name."]}

    # Dummy logic
    return {
        "recommendations": [
            f"{whiskey_name} Reserve",
            f"{whiskey_name} Select",
            f"{whiskey_name} Barrel Strength"
        ]
    }