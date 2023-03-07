from flask import Blueprint

alumnnos = Blueprint('alumnos', __name__)

@alumnnos.route('/getalum', methods=['GET'])
def getalum():
    return {'key':'alumnos'}