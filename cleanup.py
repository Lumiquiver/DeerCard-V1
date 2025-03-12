import os
import logging
import yaml

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = logging.getLogger("cleanup")
logger.setLevel(logging.INFO)

log_directory = "logs/"
threat_directory = "threat_intel/"
max_log_files = config["logging"].get("backup_count", 5)

def cleanup_logs():
    log_files = sorted([f for f in os.listdir(log_directory) if f.endswith(".log")], key=lambda x: os.path.getmtime(os.path.join(log_directory, x)))
    if len(log_files) > max_log_files:
        for old_log in log_files[:-max_log_files]:
            os.remove(os.path.join(log_directory, old_log))
            logger.info(f"Deleted old log file: {old_log}")

def cleanup_threat_signatures():
    threat_file = os.path.join(threat_directory, "honeypot_signatures.json")
    if os.path.exists(threat_file):
        os.remove(threat_file)
        logger.info("Deleted outdated threat signatures file.")

def run_cleanup():
    logger.info("Starting cleanup process...")
    cleanup_logs()
    cleanup_threat_signatures()
    logger.info("Cleanup completed.")

if __name__ == "__main__":
    run_cleanup()
