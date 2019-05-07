from google.cloud import storage
from google.oauth2 import service_account
import json


def download_from_cloud_storage():
    credentials = service_account.Credentials.from_service_account_file(
        '/secrets/private-key.json')
    try:
        client = storage.Client(
            project=credentials.project_id,
            credentials=credentials)
    except IOError:
        client = storage.Client()
    bucket = client.get_bucket('ml-prod-models')
    blob = bucket.get_blob('iris-model/lte_fe34789_20190318141552947255.pkl')
    blob.download_to_filename('/models/model.pkl')


def load_model():
    global model
    with open('/models/model.pkl', 'rb') as f:
        model = json.load(f)
