from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def get_data_from_database(page_number, items_per_page):
    conn = psycopg2.connect(
        dbname="flats",
        user="postgres",
        password="postgres",
        host="db",
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

if __name__ == "__main__":
    app.run(debug=True, port=8080)
