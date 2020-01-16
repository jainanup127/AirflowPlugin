from airflow.www.app import csrf
from flask import (
    Blueprint
)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
myapi = Blueprint('myapi', __name__)
csrf.exempt(myapi)
