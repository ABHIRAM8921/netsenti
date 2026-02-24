
# NetSentinel 🚨
Real-Time Behavioral Network Intrusion Detection System  
Designed for small institutions and lab environments.


## 📌 Overview

NetSentinel is a real-time network intrusion detection system that uses:

- Zeek (Packet + Flow Analysis)
- Python (Anomaly Detection + Classification)
- Elasticsearch (Log Storage)
- FastAPI (Admin API)
- Web Dashboard (Threat Monitoring)

It detects:
- Port Scanning
- Brute Force Attempts
- Data Exfiltration
- Behavioral Anomalies



# ⚙️ SYSTEM REQUIREMENTS

Recommended:

- Ubuntu 22.04 / 24.04
- 8GB RAM minimum (16GB recommended)
- 50GB Disk
- 2 Network Interfaces (optional but recommended)


# 🛠 INSTALLATION GUIDE

## STEP 1 — Update System

```bash
sudo apt update && sudo apt upgrade -y
````


## STEP 2 — Install Dependencies

```bash
sudo apt install -y \
cmake make gcc g++ flex bison \
libpcap-dev libssl-dev python3-dev swig \
zlib1g-dev bind9-dev libkrb5-dev \
libmaxminddb-dev libc-ares-dev \
python3-pip git curl wget
```


## STEP 3 — Install Zeek (Official Source)

```bash
wget https://download.zeek.org/zeek-6.0.3.tar.gz
tar -xvzf zeek-6.0.3.tar.gz
cd zeek-6.0.3
./configure
make -j$(nproc)
sudo make install
```

Add Zeek to PATH:

```bash
echo 'export PATH=$PATH:/usr/local/zeek/bin' >> ~/.bashrc
source ~/.bashrc
```

Verify:

```bash
zeek --version
```


## STEP 4 — Configure Zeek Interface

Check interface:

```bash
ip a
```

Edit:

```bash
sudo nano /usr/local/zeek/etc/node.cfg
```

Set correct interface:

```
interface=eth0
```

(Replace eth0 with your actual interface.)


## STEP 5 — Install Elasticsearch

```bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.11.0-amd64.deb
sudo dpkg -i elasticsearch-8.11.0-amd64.deb
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch
```

Reduce memory (important):

```bash
sudo nano /etc/elasticsearch/jvm.options
```

Change:

```
-Xms512m
-Xmx512m
```

Start service:

```bash
sudo systemctl start elasticsearch
```

Verify:

```bash
curl localhost:9200
```

You should see JSON output.


## STEP 6 — Clone NetSentinel Project

```bash
git clone https://github.com/YOUR_USERNAME/NetSentinel.git
cd NetSentinel
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python packages:

```bash
pip install -r requirements.txt
```



# 🚀 RUNNING NETSENTINEL

Open 3 terminals.


## Terminal 1 — Start Elasticsearch

```bash
sudo systemctl start elasticsearch
```


## Terminal 2 — Start Zeek

```bash
sudo zeekctl deploy
```

Check logs:

```bash
ls /usr/local/zeek/logs/current/
```

You should see `conn.log`.


## Terminal 3 — Start NetSentinel

```bash
source venv/bin/activate
python run.py
```

# 🌐 Access Dashboard

API Documentation:

```
http://localhost:8000/docs
```

Threat Feed:

```
http://localhost:8000/threats
```


# 🧪 Testing The System

Generate traffic:

```bash
ping google.com
```

Simulate Port Scan:

```bash
nmap -sS localhost
```

Check stored threats:

```bash
curl -X GET "localhost:9200/netsentinel/_search?pretty"
```


# 🔥 Expected Output

Detected threats will include:

* Port Scanning
* Brute Force Attempt
* Data Exfiltration
* Anomalous Behavior

Each log contains:

* Source IP
* Destination Port
* Threat Type
* Severity
* Timestamp


# 📊 Architecture

Network → Zeek → Feature Extraction → ML Engine → Elasticsearch → Dashboard



# 🛑 Troubleshooting

If Zeek fails:

```bash
sudo zeekctl status
```

If Elasticsearch fails:

```bash
sudo systemctl status elasticsearch
```

If no logs appear:

Ensure correct network interface is set in node.cfg.

---

# 🎯 Author

NetSentinel
Real-Time Behavioral IDS
Designed for academic and research environments.
..
