from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)        # 서버가 자동 생성, 출력 전용
    title = fields.String(required=True)   # 책 제목
    author = fields.String(required=True)  # 책 저자

