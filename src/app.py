import os
from flask import Flask, Response, json
from flask import render_template, request, redirect, send_from_directory
from flaskext.mysql import MySQL
import datetime

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'democraticNews'

UPLOADS = os.path.join('src/uploads')
app.config['UPLOADS'] = UPLOADS  # guardamos la ruta como un valor de la app

mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/tabla')
def tabla():
    # Aquí deberías recuperar y pasar los datos necesarios para la tabla
    return render_template('noticias/tabla.html')

@app.route('/publish')
def publish():
    return render_template('noticias/publish.html')

@app.route('/store', methods=['POST'])
def store():

    return redirect('/')  


if __name__ == '__main__':
    app.run(debug=True)
