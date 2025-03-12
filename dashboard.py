from flask import Flask, render_template, jsonify
import yaml
import os

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

dashboard_config = config["dashboard"]

app = Flask(__name__)

LOG_FILE = config["logging"]["log_file"]
ALERT_LOG_FILE = config["logging"]["alert_log_file"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"logs": []})
    
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()[-50:]  # Get last 50 log entries
    
    return jsonify({"logs": logs})

@app.route("/alerts")
def get_alerts():
    if not os.path.exists(ALERT_LOG_FILE):
        return jsonify({"alerts": []})
    
    with open(ALERT_LOG_FILE, "r") as file:
        alerts = file.readlines()[-50:]  # Get last 50 alert entries
    
    return jsonify({"alerts": alerts})

if __name__ == "__main__":
    app.run(host=dashboard_config["host"], port=dashboard_config["port"], debug=True)
