from flask import render_template, flash
from app import app, db
from app.models.usuario import Usuario
import sqlalchemy as sa
from werkzeug.security import generate_password_hash


from app.models import Usuario

class UsuarioController:

    def salvar(formulario):
        try:
            usuario = Usuario()
            formulario.populate_obj(usuario)
            usuario.password_hash = generate_password_hash(formulario.password.data)
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
        
        
    def checar_unicidade(campo, tipo):
        if tipo == 'username':
            if Usuario.query.filter_by(username=campo).first():
                return False
        if tipo == 'email':
            if Usuario.query.filter_by(email=campo).first():
                return False
        return True