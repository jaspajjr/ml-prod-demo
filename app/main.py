from flask import Flask, jsonify, request
import uuid
import structlog
import numpy as np
import model


logger = structlog.get_logger()
APP = Flask(__name__)


def make_prediction(model, params: dict) -> dict:
    pred_array = np.array([params['v1'], params['v2'], params['v3'],
                           params['v4']])
    result = model.predict(pred_array.reshape(1, -1))[0]
    print(result)
    return {
        'result': result
    }


@APP.route("/prediction", methods=['POST'])
def prediction():
    log = logger.new(request_id=str(uuid.uuid4()))
    request_json = request.json

    log.info("request-made", request_params=request_json)

    result = make_prediction(pred_model, request_json['params'])

    log.info("prediction-made", prediction_result=result)

    return jsonify({
        "results": result,
        'request_params': request_json
        })


if __name__ == "__main__":
    model.download_from_cloud_storage()
    pred_model = model.load_model()
    APP.run(host='0.0.0.0', port=5000, debug=True)
