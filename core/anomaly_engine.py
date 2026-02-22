from sklearn.ensemble import IsolationForest
from core.threat_classifier import classify_threat, assign_severity

model = IsolationForest(contamination=0.05)

def detect_anomalies(df):

    model.fit(df[['duration', 'orig_bytes', 'conn_frequency']])
    df['anomaly_score'] = model.predict(
        df[['duration', 'orig_bytes', 'conn_frequency']]
    )

    df['threat_type'] = df.apply(classify_threat, axis=1)
    df['severity'] = df['threat_type'].apply(assign_severity)

    return df
