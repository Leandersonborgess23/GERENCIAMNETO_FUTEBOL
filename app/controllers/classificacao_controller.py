from app import db
from app.models.time import Time
from app.models.jogo import Jogo

class ClassificacaoController:
    def calcular_classificacao():
        times = Time.query.all()
        jogos = Jogo.query.all()