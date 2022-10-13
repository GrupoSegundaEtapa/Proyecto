from flask import Flask, render_template, url_for, request, flash, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
#conexion a sql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_POSSWORD'] = ' '
app.config['MYSQL_DB'] = 'pytes'
mysql = MySQL(app)

#setting
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('add_tarea', methodos = ['POST'])
def agregar_tarea():
    if request.method == 'POST':
        tarea = request.form['tarea']
        descripcion  = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tareas (tareas, descripcion) VALUES (%s, %s)', (tarea, descripcion))
        mysql.connection.commit()
        flash("Recibido Correctamente")
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=5000, debug = True)