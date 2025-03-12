from flask import Flask, jsonify, request
import yaml
import os

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

api_config = config["api"]

app = Flask(__name__)

LOG_FILE = config["logging"]["log_file"]
ALERT_LOG_FILE = config["logging"]["alert_log_file"]

def read_logs(log_file, num_lines=50):
    if not os.path.exists(log_file):
        return []
    
    with open(log_file, "r") as file:
        return file.readlines()[-num_lines:]

@app.route("/api/logs", methods=["GET"])
def get_logs():
    return jsonify({"logs": read_logs(LOG_FILE)})

@app.route("/api/alerts", methods=["GET"])
def get_alerts():
    return jsonify({"alerts": read_logs(ALERT_LOG_FILE)})

@app.route("/api/threats", methods=["GET"])
def get_threats():
    threat_file = "threat_intel/honeypot_signatures.json"
    if not os.path.exists(threat_file):
        return jsonify({"threats": []})
    
    with open(threat_file, "r") as file:
        return jsonify({"threats": file.read()})

@app.route("/api/alerts", methods=["POST"])
def post_alert():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Missing alert message"}), 400
    
    alert_message = data["message"]
    with open(ALERT_LOG_FILE, "a") as file:
        file.write(alert_message + "\n")
    
    return jsonify({"status": "Alert logged successfully"})

if __name__ == "__main__":
    app.run(host=api_config["host"], port=api_config["port"], debug=True)
