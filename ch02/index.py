from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study_1')
cur = conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")
@app.post("/save")
def up():
    num = request.get_json("num")
    cur.execute(f"insert into numcount(num) values({num["num"]});")
    conn.commit()
    return str(num["num"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
    cur.close()
    conn.close()
