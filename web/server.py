from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Usuarios_inscritos')
def USUARIO():
    db_session = db.getSession(engine)
    USUARIO = db_session.query(entities.USUARIO)
    data = USUARIO[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/Crear_nuevo_usuario', methods = ['GET'])
def Crear_nuevo_usuario():
    db_session = db.getSession(engine)
    USUARIO = entities.USUARIO(codigo="20181013", nombre = "Said", apellido="Choquehuanca", contrasena="Ut3c14")
    db_session.add(USUARIO)
    db_session.commit()
    return "Usuario creado!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug=True,port=8080, threaded=True)
