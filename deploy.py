import os
import subprocess
import yaml
import logging

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logger = logging.getLogger("deploy")
logger.setLevel(logging.INFO)

# Deployment settings
env = config.get("environment", "production")
repo_url = config["deployment"]["repo_url"]
install_requirements = config["deployment"].get("install_requirements", True)

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        logger.info(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {command} - {e}")

def clone_or_update_repo():
    if os.path.exists("deercard/"):
        os.chdir("deercard/")
        run_command("git pull origin main")
    else:
        run_command(f"git clone {repo_url} deercard/")
        os.chdir("deercard/")

def setup_environment():
    if install_requirements:
        run_command("pip install -r requirements.txt")

def start_application():
    run_command("nohup python main.py &")
    logger.info("DeerCard application started.")

def deploy():
    logger.info("Starting deployment...")
    clone_or_update_repo()
    setup_environment()
    start_application()
    logger.info("Deployment completed.")

if __name__ == "__main__":
    deploy()
