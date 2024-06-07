from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
db = SQLAlchemy()