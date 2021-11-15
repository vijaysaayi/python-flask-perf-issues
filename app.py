import logging
import math
import requests
from flask import Flask, jsonify
from datetime import  datetime
app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", level=logging.INFO)
import os, time

@app.route("/")
def hello():
    return f"PID - {os.getpid()} : Welcome to Azure App Service !"

@app.route("/slow_compute")
def slow_compute():
    n = 1
    while n < 3:
        startTime = datetime.now()
        while (datetime.now() - startTime).seconds < 18:
            math.factorial(100) 
        time.sleep(0.2)
        n += 1
    return "Slow request completed"

@app.route("/slow")
def slow_external():
    weather_report = get_weather_forecast()    
    
    if(weather_report.status_code == 200):
        return jsonify(weather_report.json())
    else:
        return f"{weather_report.status_code}"

def get_weather_forecast():
    url = "https://exp-win-wa.azurewebsites.net/weatherforecast"
    logging.info(f"Calling url {url} ..")
    response = requests.get(url)
    return response
