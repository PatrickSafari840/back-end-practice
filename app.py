from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, message TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form['name']
    message = request.form['message']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO comments (name, message) VALUES (?, ?)', (name, message))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/view_comments.html')
def view_comments():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT name, message FROM comments')
    comments = c.fetchall()
    conn.close()
    return render_template('view_comments.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
