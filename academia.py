#!C:\Users\tms1c\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html\n\n")

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'academia'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/consul_login')
def consul_login():
    if request.method=='POST':
        user = request.form['userMail']
        passw = request.form['userPw']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE email_user = ',user,' and pass_user = ', passw,' (%s, %s, %s)', (user, passw))
        mysql.connection.commit()
        if cursor.result()>0:
            return render_template('foro.html')


@app.route('/registro')
def registro():
    return render_template('form_registro.html')

@app.route('/consul_registro', methods=['GET', 'POST'])
def consul_registro():
    if request.method=='POST':
        nombre = request.form['user']
        email = request.form['email']
        contrasena = request.form['password']   
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuarios (nombre_user, email_user, pass_user) VALUES (%s, %s, %s)', (nombre, email, contrasena))
        mysql.connection.commit()
        return render_template('login.html')



if __name__ == '__main__':
    app.run(port=5500, debug=True)