import os
from flask import Flask, Response, json, url_for
from flask import render_template, request, redirect, send_from_directory
from flask_cors import CORS
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import datetime

import pymysql

app = Flask(__name__)
CORS(app)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'democraticNews'

UPLOADS = os.path.join('src/uploads')
app.config['UPLOADS'] = UPLOADS  # guardamos la ruta como un valor de la app

mysql.init_app(app)

# Conectar sin especificar la base de datos para crearla si no existe
try:
    temp_conn = pymysql.connect(
        host=app.config['MYSQL_DATABASE_HOST'],
        user=app.config['MYSQL_DATABASE_USER'],
        password=app.config['MYSQL_DATABASE_PASSWORD']
    )
    temp_cursor = temp_conn.cursor()
    temp_cursor.execute("CREATE DATABASE IF NOT EXISTS democraticnews;")
    temp_conn.commit()
    temp_cursor.close()
    temp_conn.close()
except Exception as err:
    print("Error al crear la base de datos:", err)

# Ahora conectarse normalmente con la base de datos especificada
with app.app_context():
    conn = mysql.connect()
    cursor = conn.cursor()

    # Usar la base de datos especificada
    try:
        cursor.execute("USE democraticnews;")
    except Exception as err:
        print("Error al usar la base de datos:", err)

    # Leer el contenido del archivo y guardarlo en una variable
    with open(r'src\querys.sql', 'r') as archivo:
        creationQuery = archivo.read()

    # Ejecutar cada consulta en el archivo .sql
    for query in creationQuery.split(';'):
        if query.strip():  # Evita ejecutar consultas vacías
            cursor.execute(query.strip() + ';')

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/fotodeusuario/<path:nombreFoto>')
def uploads (nombreFoto):
    return send_from_directory(os.path.join('uploads'),nombreFoto)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/delete/<int:id>')
def delete_noticia(id):
        # Se obtienen todas las noticias
    conn = mysql.connect()
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute("DELETE FROM noticias WHERE id = %s;", id)
    cursor.execute("SELECT * FROM noticias;")
    noticias = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('tabla.html', noticias=noticias)

@app.route('/tabla')
def tabla():
    # Se obtienen todas las noticias
    conn = mysql.connect()
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute("SELECT * FROM noticias;")
    noticias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('tabla.html', noticias=noticias)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/store',methods=['POST'])
def store():
    data = request.get_json()
    print(data)
    _nombre=data.get('nombre')
    _apellido=data.get('apellido')
    _correo=data.get('email')
    _gender=data.get('gender')
    _titulo=data.get('titular')
    _subtitulo=data.get('subtitulo')
    _tipo=data.get('tipo')
    _descripcion=data.get('descripcion')
    _foto=data.get('imagen')

    sql="INSERT INTO noticias (nombre, apellido, correo, gender, titulo, subtitulo, tipo, imagen, cuerpo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

    datos=(_nombre, _apellido,_correo,_gender, _titulo,_subtitulo, _tipo, _foto, _descripcion)
    conn = mysql.connect()  # Llama a la función connect()
    cursor = conn.cursor()  # Obtiene el cursor de la conexión

    print(sql)
    cursor.execute(sql,datos)

    conn.commit()

    print("se guardo la noticia")


    return redirect('/tabla')


if __name__ == '__main__':
    app.run(debug=True)
