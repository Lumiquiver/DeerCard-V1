import smtplib
import requests
import yaml
from logging import getLogger
from email.mime.text import MIMEText

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = getLogger("deercard")

def send_email_alert(subject, message):
    if not config["alerting"].get("enable_email", False):
        return
    
    try:
        smtp_server = config["alerting"]["email"]["smtp_server"]
        smtp_port = config["alerting"]["email"]["smtp_port"]
        sender_email = config["alerting"]["email"]["sender_email"]
        recipient_email = config["alerting"]["email"]["recipient_email"]
        username = config["alerting"]["email"]["username"]
        password = config["alerting"]["email"]["password"]
        
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        logger.info(f"Email alert sent to {recipient_email}")
    except Exception as e:
        logger.error(f"Failed to send email alert: {e}")

def send_slack_alert(message):
    if not config["alerting"].get("enable_slack", False):
        return
    
    try:
        webhook_url = config["alerting"]["slack"]["webhook_url"]
        payload = {"text": message}
        requests.post(webhook_url, json=payload)
        logger.info("Slack alert sent")
    except Exception as e:
        logger.error(f"Failed to send Slack alert: {e}")

def send_telegram_alert(message):
    if not config["alerting"].get("enable_telegram", False):
        return
    
    try:
        bot_token = config["alerting"]["telegram"]["bot_token"]
        chat_id = config["alerting"]["telegram"]["chat_id"]
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        requests.post(url, json=payload)
        logger.info("Telegram alert sent")
    except Exception as e:
        logger.error(f"Failed to send Telegram alert: {e}")

def send_alert(message):
    logger.warning(f"ALERT: {message}")
    send_email_alert("DeerCard Alert", message)
    send_slack_alert(message)
    send_telegram_alert(message)
