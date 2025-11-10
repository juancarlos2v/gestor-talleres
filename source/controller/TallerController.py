from flask import Blueprint,url_for,request, render_template, jsonify,redirect
from services.TallerService import TallerService

taller_bp = Blueprint('talleres', __name__, url_prefix='/talleres')

service = TallerService()

@taller_bp.route('/', methods=['GET'])
def listar_talleres():
    talleres = service.repo.get_all()
    return render_template("talleres.html", talleres=talleres)
    # return jsonify([{"id": t.id, "nombre": t.nombre, "cupo": t.cupo} for t in talleres])

@taller_bp.route('/nuevo',methods=['POST'])
def crear_taller():
    nombre= request.form["nombre"]
    modalidad=request.form["modalidad"]
    cupo=request.form["cupo"]
    fecha = request.form['fecha']
    service.crear_taller(nombre,modalidad,cupo,fecha)
    return redirect(url_for("talleres.listar_talleres"))

@taller_bp.route('/editar/<int:id>', methods=['POST'])
def editar_taller(id):
    nombre = request.form['nombre']
    modalidad = request.form['modalidad']
    cupo = request.form['cupo']
    fecha = request.form['fecha']
    service.editar_taller(id, nombre, modalidad, cupo, fecha)
    return redirect(url_for('talleres.listar_talleres'))



@taller_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_taller(id):
    service.eliminar_taller(id)
    return redirect(url_for('talleres.listar_talleres'))