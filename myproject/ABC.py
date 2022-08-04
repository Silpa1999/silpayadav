import psycopg2
from flask import Flask, request
from flask import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import json

app = Flask(__name__)
api = Api(app)


Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5433/postgres"

# disable sqlalchemy pool using NullPool as by default Postgres has its own pool
engine = create_engine(database_url, echo=True, poolclass=NullPool)

Session = sessionmaker(bind=engine)
session = Session()

# original table
class StudentInfo(Base):
    __tablename__ = 'studentdetails'
    stuName = Column("name", String)
    gender = Column("gender", String)
    age = Column("age", Integer)
    mobile = Column("mobile", Integer , primary_key = True)

# @app.route('/fetch-student-info', methods=['GET'])
# def home():
#     results = session.query(StudentInfo).all()
#     return str(results)


@app.route('/fetch-student_name', methods=['PATCH'])
def update_age():
    name = request.args.get('stuName')
    age = request.args.get('age')
    session.query(StudentInfo).filter(StudentInfo.stuNameame==name).update({"age":age})
    session.commit()
    return "age has been updated"

app.run(debug=False)