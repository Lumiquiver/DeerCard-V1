import logging
import logging.handlers
import yaml

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

log_file = config["logging"]["log_file"]
alert_log_file = config["logging"]["alert_log_file"]
max_size = 5 * 1024 * 1024  # 5MB
backup_count = config["logging"].get("backup_count", 5)

def setup_rotating_logger(log_file):
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    return handler

def rotate_logs():
    logger = logging.getLogger("log_rotation")
    logger.setLevel(logging.INFO)
    logger.addHandler(setup_rotating_logger(log_file))
    logger.addHandler(setup_rotating_logger(alert_log_file))
    logger.info("Log rotation setup completed.")

if __name__ == "__main__":
    rotate_logs()
