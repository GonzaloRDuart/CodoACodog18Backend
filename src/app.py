import os
from flask import Flask, Response, json
from flask import render_template,request,redirect, send_from_directory
from flaskext.mysql import MySQL
import datetime

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'democraticNews'

UPLOADS=os.path.join('src/uploads')
app.config['UPLOADS'] = UPLOADS #guardamos la ruta como un valor de la app

mysql.init_app(app)

@app.route('/')
def getNoticias():
    conn = mysql.connect()  # Llama a la función connect()
    cursor = conn.cursor()  # Obtiene el cursor de la conexión

    getQuery = "SELECT * FROM news;"
    cursor.execute(getQuery)

    noticias = cursor.fetchall()

    response_object = {
        'content': noticias
    }
    response = Response(json.dumps(response_object), status=200, mimetype='application/json')
    
    return response

@app.route('/postNews',methods=['POST'])
def postNews():
    _name=request.form['name']
    _lastName=request.form['lastName']
    _email=request.form['email']
    _gender=request.form['email']
    _title=request.form['title']
    _subtitle=request.form['subtitle']
    _body=request.form['body']
    _type=request.form['type']
    _imageUrl=request.form['imageUrl']

    insertQuery="INSERT INTO news (name, lastName, email, gender, title, subtitle, type, imageUrl, body, upVotes, downVotes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, 0, 0);"

    datos=(_name, _lastName, _email, _gender, _title, _subtitle, _type, _imageUrl, _body)
    conn = mysql.connect()  # Llama a la función connect()
    cursor = conn.cursor()  # Obtiene el cursor de la conexión

    cursor.execute(insertQuery,datos)
    conn.commit()
    
    return Response("OK", status=200, mimetype='text/plain')

@app.route('/delete/<title>')
def delete(title):
    conn = mysql.connect()
    cursor = conn.cursor()

    deleteQuery = "DELETE FROM news WHERE title=%s;"
   
    cursor.execute(deleteQuery, (title,))
    conn.commit()
    return Response("OK", status=200, mimetype='text/plain')

@app.route('/addUpVote/<title>')
def addVote(title):

    updateUpVotesQuery=f'UPDATE news SET upVotes = upVotes + 1 WHERE title = {title};'
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute(updateUpVotesQuery)
    conn.commit()

    return Response("OK", status=200, mimetype='text/plain')

@app.route('/addDownVote/<title>')
def addVote(title):

    updateUpVotesQuery=f'UPDATE news SET upVotes = downVotes + 1 WHERE title = {title};'
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute(updateUpVotesQuery)
    conn.commit()

    return Response("OK", status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True)
