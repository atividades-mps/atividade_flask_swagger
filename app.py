from flask import Flask
from flask_cors import CORS

from src.api.routes.events import events_blueprint
from src.api.routes.users import users_blueprint

app = Flask(__name__)
CORS(app)

@app.get('/')
def home():
    return {
        "hello": "cronologus user :D"
    }

app.register_blueprint(users_blueprint)
app.register_blueprint(events_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
