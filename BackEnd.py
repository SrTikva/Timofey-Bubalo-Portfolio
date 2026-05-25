from flask import Flask, request, redirect, url_for, render_template
import sqlite3
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_db():
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'users.db'))
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, Name TEXT,TechnicMission TEXT,TgAcc TEXT,Price INTEGER)')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        technicmission = request.form.get('request')
        tgacc = request.form.get('tgacc')
        price = request.form.get('price')
        if name:
            conn = sqlite3.connect(os.path.join(BASE_DIR, 'users.db'))
            conn.execute('INSERT INTO users (Name, TechnicMission, TgAcc, price) VALUES (?, ?, ?, ?)', (name,technicmission,"@"+tgacc, price))
            conn.commit()
            conn.close()
        return redirect(url_for('index'))
    return render_template('Index.Html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)