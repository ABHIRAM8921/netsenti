def classify_threat(row):

    if row['conn_frequency'] > 100:
        return "Port Scanning"

    if row['orig_bytes'] > 10000000:
        return "Data Exfiltration"

    if row['duration'] < 1 and row['conn_frequency'] > 50:
        return "Brute Force Attempt"

    if row['anomaly_score'] == -1:
        return "Anomalous Behavior"

    return "Normal"


def assign_severity(threat):

    severity_map = {
        "Port Scanning": "Medium",
        "Data Exfiltration": "High",
        "Brute Force Attempt": "High",
        "Anomalous Behavior": "Low",
        "Normal": "None"
    }

    return severity_map.get(threat, "Low")
