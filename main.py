import logging
import yaml
import subprocess
from logging import getLogger
from threading import Thread
from dashboard import app as dashboard_app
from api import app as api_app
from update_signatures import update_threat_signatures
from fake_activity import run_simulation

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = getLogger("deercard")
logger.setLevel(logging.INFO)

def start_flask_app(flask_app, host, port):
    flask_app.run(host=host, port=port, debug=False, use_reloader=False)

def start_services():
    logger.info("Starting DeerCard services...")
    
    # Start the API service
    api_thread = Thread(target=start_flask_app, args=(api_app, config["api"]["host"], config["api"]["port"]))
    api_thread.start()
    logger.info("API service started.")
    
    # Start the Dashboard service
    dashboard_thread = Thread(target=start_flask_app, args=(dashboard_app, config["dashboard"]["host"], config["dashboard"]["port"]))
    dashboard_thread.start()
    logger.info("Dashboard service started.")
    
    # Update threat signatures
    update_threat_signatures()
    
    # Start attack simulation (optional, can be disabled in config)
    if config.get("simulation", {}).get("enabled", False):
        simulation_thread = Thread(target=run_simulation, args=(5, 10))
        simulation_thread.start()
        logger.info("Fake attack simulation started.")
    
    logger.info("DeerCard system fully operational.")

if __name__ == "__main__":
    start_services()
