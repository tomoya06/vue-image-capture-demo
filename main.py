from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/poster/upload", methods=["POST"])
@cross_origin()
def upload():
    upload_image = request.files['file'].read()
    print(upload_image)
    res = dict()
    res['status'] = 'OK'
    res['data'] = 'ok'
    return jsonify(res)


if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=8081)
