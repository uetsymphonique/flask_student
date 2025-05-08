from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Cấu hình DB
DB_CONFIG = {
    'host': 'localhost',
    'user': 'stuuser',
    'password': 'StuP@ssw0rd!',
    'db': 'studentdb',
    'charset': 'utf8mb4'
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, email, course FROM students")
        students = cur.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (name,email,course) VALUES (%s,%s,%s)",
                        (name,email,course))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=('GET','POST'))
def edit(id):
    conn = get_conn()
    with conn.cursor() as cur:
        if request.method == 'POST':
            cur.execute("UPDATE students SET name=%s,email=%s,course=%s WHERE id=%s",
                        (request.form['name'],
                         request.form['email'],
                         request.form['course'],
                         id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        cur.execute("SELECT id,name,email,course FROM students WHERE id=%s", (id,))
        student = cur.fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM students WHERE id=%s", (id,))
        conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
