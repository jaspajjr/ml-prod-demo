from flask import Flask, jsonify
from google.oauth2 import service_account
import model


APP = Flask(__name__)


@APP.route("/prediction", methods=['GET', 'POST'])
def prediction():
    return jsonify("Hello Jasper")


if __name__ == "__main__":
    credentials = service_account.Credentials.from_service_account_file(
        '/secrets/private-key.json')
    model.download_from_cloud_storage(credentials)
    APP.run(host='0.0.0.0', port=5000, debug=True)
