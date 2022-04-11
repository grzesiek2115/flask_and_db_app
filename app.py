from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='10.0.2.15', port=5432, database='postgres', user=os.environ['DB_USERNAME'], password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.books;')
    books = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run()
