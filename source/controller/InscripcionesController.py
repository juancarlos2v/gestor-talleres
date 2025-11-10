from flask import Blueprint,url_for,request, render_template, jsonify,redirect
from services.InscripcionesService import InscripcionService

inscripcion_bp = Blueprint('inscripciones', __name__, url_prefix='/inscripciones')

service = InscripcionService()


@inscripcion_bp.route('/',methods=['GET'])
def inscripciones_list():
    inscripciones = service.obtener_todas()
    return render_template("inscripciones.html", inscripciones=inscripciones)


@inscripcion_bp.route("/", methods=["POST"])
def crear_inscripcion():
    pass