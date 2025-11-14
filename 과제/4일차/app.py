from flask import Flask
from posts_routes import posts_bp

app = Flask(__name__)
app.secret_key = "dev-secret"

app.register_blueprint(posts_bp)


if __name__ == "__main__":
    app.run(debug=True)
