from flask import Flask
from flask_restful import Api
from Controller.Ocr import Ocr
from flask_cors import CORS
from Controller.Auth import Login,CheckToken


app = Flask(__name__)
'lấy dữ liệu từ angular'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)
api.add_resource(Ocr, '/api/v1/user/ocr')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(CheckToken,"/api/v1/auth/checktoken")

if __name__ == '__main__':
    app.run(debug=True)
