import random
import time
import logging
import yaml
from logging import getLogger

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = getLogger("deercard")

fake_ips = [
    "192.168.1.100", "203.0.113.45", "198.51.100.23",
    "172.16.254.1", "10.0.0.200", "185.199.108.153"
]

fake_usernames = ["admin", "root", "user", "test", "guest"]
fake_passwords = ["123456", "password", "admin", "root", "letmein"]

def generate_fake_attack():
    ip = random.choice(fake_ips)
    username = random.choice(fake_usernames)
    password = random.choice(fake_passwords)
    attack_type = random.choice(["SSH Brute Force", "SQL Injection", "XSS Attack", "Port Scanning"])
    message = f"Suspicious activity detected: {attack_type} from {ip} using username '{username}' and password '{password}'"
    
    logger.warning(message)
    return message

def run_simulation(interval=5, iterations=10):
    for _ in range(iterations):
        generate_fake_attack()
        time.sleep(interval)

if __name__ == "__main__":
    run_simulation()
