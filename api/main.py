from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch("http://localhost:9200")

@app.get("/threats")
def get_threats():
    response = es.search(
        index="netsentinel",
        body={"query": {"match_all": {}}}
    )
    return response['hits']['hits']
