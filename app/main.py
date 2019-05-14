from flask import Flask, jsonify, request
import uuid
import structlog
import model


logger = structlog.get_logger()
APP = Flask(__name__)


@APP.route("/prediction", methods=['POST'])
def prediction():
    log = logger.new(request_id=str(uuid.uuid4()))
    request_json = request.json

    log.info("prediction-made", request_params=request_json)

    return jsonify({"results": "Hello Jasper"})


if __name__ == "__main__":
    model.download_from_cloud_storage()
    APP.run(host='0.0.0.0', port=5000, debug=True)
