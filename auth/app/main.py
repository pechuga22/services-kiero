
from flask import Flask, jsonify, request
from flask_cors import CORS

import users

app = Flask(__name__)
app.secret_key = '1298eh1089e1209e1i2ue0912e'
app.config['MEDIA_FOLDER'] = "media/"
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024    # MAX 128 MB
CORS(app, supports_credentials=True)
app.config["JSON_SORT_KEYS"] = False


@app.route('/login/getUser/', methods=['POST'])
def login():
    print("login")
    print(request)
    if request.json is None:
        return ""
    user = request.json.get("email")
    pw = request.json.get("password")

    return jsonify(users.login(user, pw, ""))


@app.route('/register/user/', methods=['POST', 'OPTION', 'OPTIONS'])
def register():

    if request.json is None:
        return ""

    name = request.json.get("name")
    last_name = request.json.get("lastname")
    nickname = request.json.get("email")
    email = request.json.get("email")
    ip = request.remote_addr

    result = False

    if "type_register" in request.json:
        rtype = request.json.get("type_register")
        if rtype == "g02":
            google_id = request.json.get("id_google")
            result = users.register_social(name, last_name, nickname, email, ip, google_id)
        elif rtype == "f03":
            facebook_id = request.json.get("id_facebook")
            result = {"recordset": users.register_social(name, last_name, nickname, email, ip, facebook_id)}
        else:
            pass
    else:
        passw = request.json.get("password")
        result = users.register_basic(name, last_name, nickname, email, passw, ip)

    if result:
        return jsonify({"message": "Usuario ok", "data": result})
    else:
        return jsonify({"message": "Error al registrar usuario"})

    # return jsonify({"Res  ultados": users.register(name, last_name, nickname, email, passw, ip)})


@app.route('/select/user/', methods=['GET'])
def select_user():
    return jsonify({"message": "usuarios", "data": users.get_user_id(request.json.get("id"))})


@app.route('/user/getAddress', methods=['POST'])
def get_address():
    return jsonify({"Resultados": None})


@app.route('/createAddress/user', methods=['POST'])
def create_address():
    return jsonify({"Resultados": None})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)
