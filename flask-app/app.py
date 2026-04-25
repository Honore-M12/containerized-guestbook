import os
import psycopg2
from flask import Flask, request, redirect
from prometheus_client import Counter , Gauge, Histogram
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)


metrics = PrometheusMetrics(app)
MESSAGES_SUBMITTED = Counter ('messages_submitted_total', 'Total number of submited messages since the start')
MESSAGES_IN_DB = Gauge ('messages_in_database_count',  'Total number of message in the database')
MESSAGE_LENGTH = Histogram ('message_length_chars', 'Distribution of message lenght')


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
    query = "SELECT content, created_at FROM messages ORDER BY created_at DESC"
    cur.execute(query)
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
        MESSAGES_[SUBMITTED.inc](http://SUBMITTED.inc)()
        MESSAGE_LENGTH.observe(len(message))
        cur.execute("SELECT COUNT(*) FROM messages")
        total = cur.fetchone()[0]  
        MESSAGES_IN_DB.set(total)
        cur.close()
        conn.close()
    return redirect("/")
if __name__ == "__main__":
    init_db()
    [app.run](http://app.run)(host="0.0.0.0", port=5000)
