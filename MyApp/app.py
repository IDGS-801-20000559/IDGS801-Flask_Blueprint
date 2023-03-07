from flask import Flask, jsonify, render_template
from flask import request
from flask import redirect
from flask import url_for

# Referencia a los funciones de los módulos
from alumnos.routes import alumnnos
from directivos.routes import dir
from maestros.routes import maestros

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def home():
    return jsonify({'Datos': 'Hola'})

#Registra a los módulos
app.register_blueprint(alumnnos)
app.register_blueprint(dir)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run()