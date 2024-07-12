import os
from flask import Flask, Response, json, url_for
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

@app.route('/tabla')
def tabla():
    # Se obtienen todas las noticias
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM noticias;")
    noticias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('noticias/tabla.html', noticias=noticias)

@app.route('/create')
def create():
    return render_template('noticias/create.html')

@app.route('/publish')
def publish():
    return render_template('noticias/publish.html')

@app.route('/store',methods=['POST'])
def store():
    _nombre=request.form['nombre']
    _apellido=request.form['apellido']
    _correo=request.form['email']
    _titulo=request.form['titular']
    _subtitulo=request.form['subtitulo']
    _cuerpo=request.form['descripcion']
    _foto=request.files['imagen']
    
   # Suponiendo que _foto es una instancia de werkzeug.datastructures.FileStorage
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Crear el directorio 'uploads' si no existe
    upload_dir = 'src/uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    if _foto.filename != '':
        nuevoNombreFoto= f"{timestamp}_{_foto.filename}"
         # Guardar la foto en el sistema de archivos
        _foto.save(os.path.join(upload_dir, nuevoNombreFoto))

    sql="INSERT INTO noticias (nombre, apellido, correo, titulo, subtitulo, imagen, cuerpo) VALUES (%s,%s,%s,%s,%s,%s,%s);"

    datos=(_nombre, _apellido,_correo,_titulo,_subtitulo, nuevoNombreFoto,_cuerpo)
    conn = mysql.connect()  # Llama a la función connect()
    cursor = conn.cursor()  # Obtiene el cursor de la conexión

    cursor.execute(sql,datos)
    conn.commit()


    return redirect('noticias/tabla.html')


if __name__ == '__main__':
    app.run(debug=True)
