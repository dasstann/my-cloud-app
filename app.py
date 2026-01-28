import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Получаем URL базы из переменных окружения
DB_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DB_URL)

@app.route('/')
def index():
    if not DB_URL:
        return "<h1>База данных не настроена!</h1>"
    
    conn = get_db_connection()
    cur = conn.cursor()
    # Создаем таблицу, если её нет
    cur.execute('CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, time timestamp DEFAULT CURRENT_TIMESTAMP);')
    # Добавляем запись о визите
    cur.execute('INSERT INTO visits DEFAULT VALUES;')
    conn.commit()
    # Считаем общее кол-во
    cur.execute('SELECT COUNT(*) FROM visits;')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    
    return f"<h1>Hello Cloud!</h1><p>Это посещение номер: <b>{count}</b></p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)