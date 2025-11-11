from flask import Flask
from flask_smorest import Api
from api import book_blp

app = Flask(__name__)

# Swagger/OpenAPI 설정
app.config['API_TITLE'] = 'Book API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(book_blp)

if __name__ == '__main__':
    # OS가 사용 가능한 포트를 자동 선택
    app.run(host="127.0.0.1", port=0, debug=True)
