import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from flask_wtf import CSRFProtect

app = Flask(__name__)
CORS(app)

def get_data_from_database(page_number=1, items_per_page=24):
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USERNAME"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT")
    )
    cursor = conn.cursor()
    offset = (page_number - 1) * items_per_page
    cursor.execute("SELECT title, image_url FROM flats LIMIT %s OFFSET %s;", (items_per_page, offset))
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.route("/api/data", methods=["GET"])
def get_data():
    page_number = int(request.args.get("page", 1))
    items_per_page = int(request.args.get("items_per_page", 10))
    data = get_data_from_database(page_number, items_per_page)
    return jsonify(data)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.config['CSRF_ENABLED'] = True

# Set the CSRF_SESSION_KEY setting to a unique value.
app.config['CSRF_SESSION_KEY'] = 'my_secret_key'

# Add the CSRFProtect extension to the application.
csrf = CSRFProtect(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)