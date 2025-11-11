from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {"name": "가나디"},
        {"name": "최고심"},
        {"name": "농담곰"},
        {"name": "메타몽"}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
