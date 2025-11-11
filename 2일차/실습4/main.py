from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello')
def hello():
    """
    Hello API
    ---
    responses:
      200:
          description: 성공 응답
      schema:
          type: object
          properties:
              message:
                  type: string
                  example: "Hello, OZ!"
    """
    return jsonify({"message": "Hello, OZ!"})


if __name__ == "__main__":
    app.run(debug=True)

    # http://127.0.0.1:5000/apidocs 접속하면 스웨거 api 작성완료