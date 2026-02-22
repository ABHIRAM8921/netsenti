import pandas as pd
from core.anomaly_engine import detect_anomalies
from core.elastic_handler import send_to_elastic

def process_log(log_path):
    df = pd.read_csv(log_path, sep="\t", comment="#")

    if df.empty:
        return

    df['conn_frequency'] = df.groupby('id.orig_h')['id.orig_h'].transform('count')

    features = df[['id.orig_h', 'id.resp_p', 'duration', 'orig_bytes', 'conn_frequency']]

    results = detect_anomalies(features)

    for _, row in results.iterrows():
        send_to_elastic(row.to_dict())
