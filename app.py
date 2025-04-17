from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('tasks.db')

@app.route('/create_task', methods=['POST'])
def create_task():
    data = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, deadline, priority) 
        VALUES (?, ?, ?, ?)
    """, (data['title'], data['description'], data['deadline'], data['priority']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarefa criada com sucesso!"})

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

if __name__ == '__main__':
    conn = connect_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            deadline DATE NOT NULL,
            priority TEXT NOT NULL
        )
    """)
    conn.close()
    app.run(debug=True)