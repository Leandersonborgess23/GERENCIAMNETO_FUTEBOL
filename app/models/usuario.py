from app import db  #importa o objeto db da aplicação Flask, criado em app/__init__.py
import sqlalchemy as sa  #importa o módulo SQLAlchemy, renomeado como sa
import sqlalchemy.orm as so  #importa o módulo de mapeamento objeto-relacional (ORM) como so
from typing import Optional  #importa Optional, do módulo typing. Permite indicar que um campo pode ser None (nulo)
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):  #define a classe Usuario, que herda de db.Model. Essa classe representará uma tabela no banco de dados
    id: so.Mapped[int] = so.mapped_column(primary_key=True)  #define a coluna id como inteiro, chave primária
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)  #define a coluna username como string (até 64 caracteres), índice para aprimorar as buscas e com valor único no banco
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)  #igual ao campo anterior, mas para o email do usuário
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))  #senha codificada (hash) do usuário como string (até 256 caracteres), pode ser nula