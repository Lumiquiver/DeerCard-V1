# 🚀 DeerCard - Honeypot-Based Threat Intelligence System

![DeerCard Dashboard](https://github.com/Lumiquiver/DeerCard-V1/blob/main/deercard.png)

## 📌 Overview
DeerCard is a cybersecurity tool designed to detect, log, and alert on suspicious activities using a honeypot-based threat intelligence system. It includes a real-time dashboard, API, logging, alerting, and threat intelligence updates.

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **Configuration:** YAML
- **Logging & Alerts:** Logging, SMTP, Webhooks
- **Threat Intelligence:** JSON, Requests
- **Frontend:** HTML, JavaScript (jQuery), AJAX

---
## 🚀 Features
✅ **Centralized Configuration** - Easily configurable via `config.yaml`  
✅ **Structured Logging** - Logs attacks with timestamps & severity levels  
✅ **Real-Time Alerting** - Sends alerts via Slack, Telegram, and Email  
✅ **Web Dashboard** - Flask-based real-time UI to monitor logs & alerts  
✅ **REST API** - Provides endpoints to fetch attack logs and alerts  
✅ **Threat Intelligence Updates** - Fetches latest malicious IPs & attack signatures  
✅ **Attack Simulation** - Generates fake attack logs for testing  
✅ **Automated Deployment & Cleanup** - Deploy easily & manage logs efficiently  

---
## 🚀 Installation & Deployment
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Lumiquiver/DeerCard-V1.git
cd deercard
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure `config.yaml`
Modify `config.yaml` to set up API keys, webhook URLs, and other parameters.

### 4️⃣ Start the System
```bash
python main.py
```

### 5️⃣ Access the Dashboard
Open a browser and visit:
```
http://localhost:5000
```

---
## 📡 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/api/logs`    | GET    | Fetch logs |
| `/api/alerts`  | GET    | Fetch alerts |
| `/api/threats` | GET    | Fetch threat intelligence |
| `/api/alerts`  | POST   | Send an alert |

---
## 📖 License
MIT License © 2024 DeerCard

For contributions, feel free to submit pull requests. 🚀

