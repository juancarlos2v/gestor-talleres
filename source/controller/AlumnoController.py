from flask import Blueprint,url_for,request, render_template, jsonify,redirect,flash
from services.AlumnoService import AlumnoService
from exceptions.DatosInvalidosError import DatosInvalidosError

alumno_bp = Blueprint('alumnos', __name__, url_prefix='/alumnos')

service = AlumnoService()


@alumno_bp.route("/",methods=['GET'])
def alumnos_list():
    alumnos = service.obtener_todos()
    return render_template("alumnos.html", alumnos=alumnos)

@alumno_bp.route("/", methods=[ "POST"])
def crear_alumno():
    try:
        service.crear({
            'dni': request.form['dni'],
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido']
        })
         #flash('Alumno creado exitosamente', 'success')
        return redirect(url_for('alumnos.alumnos_list'))
    except DatosInvalidosError as e:
        flash(str(e), 'error')
        return redirect(url_for('alumnos.alumnos_list') + '#modal-alumno')