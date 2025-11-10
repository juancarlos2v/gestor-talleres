from flask import  Flask
from config.database import db
from controller.TallerController import taller_bp
from controller.AlumnoController import alumno_bp

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = '1111'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:root@127.0.0.1:3306/gestor-dsoo'
    db.init_app(app)

    app.register_blueprint(taller_bp)
    app.register_blueprint(alumno_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)




   