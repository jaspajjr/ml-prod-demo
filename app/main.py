from flask import Flask, jsonify
# from google.oauth2 import service_account
from google.cloud import storage
import json


APP = Flask(__name__)


def download_from_cloud_storage(credentials):
    client = storage.Client(project=credentials.project_id,
                            credentials=credentials)
    bucket = client.get_bucket('iris-model')
    blob = bucket.get_blob('iris-model/lte_fe34789_20190318141552947255.pkl')

    blob.download_to_filename('/models/model.pkl')


def load_model():
    global model
    with open('/models/model.pkl', 'rb') as f:
        model = json.load(f)


@APP.route("/prediction", methods=['GET', 'POST'])
def prediction():
    return jsonify("Hello World")


if __name__ == "__main__":
    # credentials = service_account.Credentials.from_service_account_file(
    #     '/secrets/private-key.json')
    # download_from_cloud_storage(credentials)
    APP.run(host='0.0.0.0', port=5000, debug=True)
