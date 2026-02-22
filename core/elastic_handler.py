from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch("http://localhost:9200")

def send_to_elastic(record):

    record['timestamp'] = datetime.now().isoformat()

    es.index(
        index="netsentinel",
        document=record
    )
