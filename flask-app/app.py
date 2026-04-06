import os
import psycopg2
from flask import Flask, request, redirect

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT content, created_at FROM messages ORDER BY created_at DESC")
    messages = cur.fetchall()
    cur.close()
    conn.close()

    html = "<h1>Guestbook</h1>"
    html += "<form method='POST' action='/add'>"
    html += "<input type='text' name='message' placeholder='Ton message...'>"
    html += "<button type='submit'>Envoyer</button>"
    html += "</form><hr>"
    for msg in messages:
        html += f"<p>{msg[0]} — <small>{msg[1]}</small></p>"
    return html

@app.route("/add", methods=["POST"])
def add():
    message = request.form.get("message")
    if message:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
