import logging
import math
from flask import Flask
from datetime import  datetime
app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", level=logging.INFO)
import os, time

@app.route("/")
def hello():
    return f"PID - {os.getpid()} : Welcome to Azure App Service !"

@app.route("/slow")
def slow_request():
    n = 1
    while n < 3:
        startTime = datetime.now()
        while (datetime.now() - startTime).seconds < 18:
            math.factorial(100) 
        time.sleep(0.2)
        n += 1
    return "Slow request completed"