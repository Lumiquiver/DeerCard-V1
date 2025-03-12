import logging
import logging.handlers
import yaml

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

log_file = config["logging"]["log_file"]
alert_log_file = config["logging"]["alert_log_file"]
log_level = getattr(logging, config["logging"]["level"].upper(), logging.INFO)
max_size = 5 * 1024 * 1024  # 5MB
backup_count = config["logging"].get("backup_count", 5)

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Main logger
logger = setup_logger("deercard", log_file, log_level)

# Alert logger
alert_logger = setup_logger("alerts", alert_log_file, log_level)

def log_event(message, level="info"):
    if level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)
    else:
        logger.info(message)

def log_alert(message, level="warning"):
    alert_logger.warning(message)  # Alerts default to warning level
