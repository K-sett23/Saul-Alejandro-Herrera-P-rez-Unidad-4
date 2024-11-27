# app.py
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='db',
        user='root',
        password='mi_contraseña',
        database='mi_base_de_datos'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form['item']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name) VALUES (%s)', (new_item,))
    conn.commit()
    conn.close()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)