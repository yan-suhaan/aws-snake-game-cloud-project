from flask import Flask, request
import pymysql
import logging

app = Flask(__name__)

logging.basicConfig(
    filename='snake.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

connection = pymysql.connect(
    host='snake-db.c900wawcofcc.ap-south-1.rds.amazonaws.com',
    user='admin',
    password='********',
    database='snake_db'
)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/save_score", methods=["POST"])
def save_score():

    player = request.form["player"]
    score = request.form["score"]

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO leaderboard
        (player_name, score)
        VALUES (%s,%s)
        """,
        (player, score)
    )
   connection.commit()

    logging.info(
        f"SCORE | Player={player} Score={score}"
    )

    return "Score Saved"

@app.route("/leaderboard")
def leaderboard():

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT player_name, score
        FROM leaderboard
        ORDER BY score DESC
        LIMIT 10
        """
    )

    data = cursor.fetchall()

    html = """
    <h1>Snake Leaderboard</h1>
    <table border='1'>
    <tr>
    <th>Player</th>
    <th>Score</th>
    </tr>
      """

    for row in data:
        html += f"""
        <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        </tr>
        """

    html += "</table>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

