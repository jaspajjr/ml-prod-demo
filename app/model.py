from google.cloud import storage
import json


def download_from_cloud_storage(credentials):
    client = storage.Client(project=credentials.project_id,
                            credentials=credentials)
    bucket = client.get_bucket('ml-prod-models')
    blob = bucket.get_blob('iris-model/lte_fe34789_20190318141552947255.pkl')
    blob.download_to_filename('/models/model.pkl')


def load_model():
    global model
    with open('/models/model.pkl', 'rb') as f:
        model = json.load(f)
