from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from connection import get_engine

app = Flask(__name__)
CORS(app)

Base = declarative_base()

class Flat(Base):
    __tablename__ = 'flats'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    image_url = Column(String)

def get_data_from_database(page_number=1, items_per_page=12):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Flat.title, Flat.image_url).limit(items_per_page).offset((page_number - 1) * items_per_page)
    result = query.all()
    session.close()

    results = [tuple(row) for row in result]
    return results

@app.route("/api/data", methods=["GET"])
def get_data():
    page_number = int(request.args.get("page", 1))
    items_per_page = int(request.args.get("items_per_page", 1))
    data = get_data_from_database(page_number, items_per_page)
    return jsonify(data)

@app.route('/')
def index():
    return 'Server is up!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
