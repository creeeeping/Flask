from flask import Flask
from flask_smorest import Api, abort
from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import Schema, fields

# -------------------- 스키마 --------------------
class BookSchema(Schema):
    id = fields.Int(dump_only=True)        # 서버가 자동 생성, 출력 전용
    title = fields.String(required=True)   # 책 제목
    author = fields.String(required=True)  # 책 저자

# -------------------- 초기 데이터 --------------------
books = [
    {"id": 1, "title": "원피스", "author": "오다 에이치로"},
    {"id": 2, "title": "소용돌이", "author": "이토 준지"},
    {"id": 3, "title": "베르세르크", "author": "미우라 켄타로"},
    {"id": 4, "title": "짱구는 못말려", "author": "요시이 우스토"},
    {"id": 5, "title": "헌터x헌터", "author": "토가시 요시히로"}
]

# -------------------- 블루프린트 --------------------
book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# -------------------- 책 목록 --------------------
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = max([b['id'] for b in books], default=0) + 1
        books.append(new_data)
        return new_data

# -------------------- 개별 책 --------------------
@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            abort(404, message="Book not found.")
        return book

    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            abort(404, message="Book not found.")
        books = [b for b in books if b['id'] != book_id]
        return ''

# -------------------- Flask 앱 --------------------
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


    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book

    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((b for b in books if b['id'] == book_id), None)
        if not book:
            abort(404, message="Book not found.")
        books = [b for b in books if b['id'] != book_id]
        return ''
