from flask import Flask, jsonify
import model


APP = Flask(__name__)


@APP.route("/prediction", methods=['GET', 'POST'])
def prediction():
    return jsonify("Hello Jasper")


if __name__ == "__main__":
    model.download_from_cloud_storage()
    APP.run(host='0.0.0.0', port=5000, debug=True)
