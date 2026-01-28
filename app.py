from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Мы имитируем получение данных (например, из БД или окружения)
    db_status = os.getenv("DB_INFO", "База данных пока не подключена")
    return f"""
    <h1>Hello, World!</h1>
    <p>Это мой первый веб-сервер в облаке.</p>
    <p>Данные из 'базы': <b>{db_status}</b></p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)