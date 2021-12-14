from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Configuration


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Home page!</h1>'


app = Flask(__name__)
app.config.from_object(Configuration)

if __name__ == '__main__':
    app.run(debug=True)
api = Api(app)
db = SQLAlchemy(app)
