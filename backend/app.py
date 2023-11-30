from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Configuration de la base de données
db = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    user=os.environ.get("DB_USER", "myuser"),
    password=os.environ.get("DB_PASSWORD", "mypassword"),
    database=os.environ.get("DB_DATABASE", "mydatabase"),
    port=int(os.environ.get("DB_PORT", 3306))
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM mytable")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
