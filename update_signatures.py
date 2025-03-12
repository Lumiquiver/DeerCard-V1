import requests
import yaml
import json
import logging

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = logging.getLogger("update_signatures")
logger.setLevel(logging.INFO)

threat_file = "threat_intel/honeypot_signatures.json"
sources = config["threat_intelligence"]["sources"]

def fetch_threat_data():
    all_signatures = []
    
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            all_signatures.extend(data)
            logger.info(f"Fetched {len(data)} threat signatures from {url}")
        except requests.RequestException as e:
            logger.error(f"Failed to fetch threat data from {url}: {e}")
    
    return all_signatures

def update_threat_signatures():
    signatures = fetch_threat_data()
    
    if signatures:
        with open(threat_file, "w") as file:
            json.dump(signatures, file, indent=4)
        logger.info(f"Updated {len(signatures)} threat signatures.")
    else:
        logger.warning("No new threat signatures were fetched.")

if __name__ == "__main__":
    update_threat_signatures()
