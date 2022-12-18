from flask import Flask
from src.user.home.api.blueprint.home import home

app = Flask(__name__,static_url_path="/")

# app.register_blueprint(home)
app.register_blueprint(home ,url_prefix = '')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)