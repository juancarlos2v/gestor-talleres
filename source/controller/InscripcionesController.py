from flask import Blueprint,url_for,request, render_template, jsonify,redirect,flash
from services.InscripcionesService import InscripcionService

inscripcion_bp = Blueprint('inscripciones', __name__, url_prefix='/inscripciones')

service = InscripcionService()


@inscripcion_bp.route('/',methods=['GET'])
def inscripciones_list():
    inscripciones = service.obtener_todas()
    talleres = service.obtener_talleres()
    return render_template("inscripciones.html", inscripciones=inscripciones,talleres=talleres)


@inscripcion_bp.route("/", methods=["POST"])
def crear_inscripcion():
    try:
        service.crear({
            'dni': int(request.form['dni']),
            'id_taller': int(request.form['id_taller'])
        })
        flash('Inscripción creada exitosamente', 'success')
    except Exception as e:
        flash(str(e), 'error')

    return redirect(url_for('inscripciones.inscripciones_list') + '#modal-inscripcion')
