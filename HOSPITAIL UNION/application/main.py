from flask import Flask,Blueprint,render_template
from src.home.api.blueprints import home

app = Flask(__name__, static_url_path="/")

app.register_blueprint()

app.register_blueprint(home)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)