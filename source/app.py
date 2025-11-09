from flask import Flask
from flask import jsonify
from config.database import db
from services.TallerService import TallerService

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:root@127.0.0.1:3306/gestor-dsoo'
db.init_app(app)

service=TallerService()

@app.route("/talleres",methods=["GET"])
def listar_tallers():
    talleres = service.repo.get_all()
    return jsonify([{"id": t.id, "nombre": t.nombre, "cupo": t.cupo} for t in talleres])
   