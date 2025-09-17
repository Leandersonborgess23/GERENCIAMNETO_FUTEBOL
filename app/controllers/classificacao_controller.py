from app import db
from app.models.time import Time
from app.models.jogo import Jogo

class ClassificacaoController:
    def calcular_classificacao():
        times = Time.query.all()
        jogos = Jogo.query.all()

        tabela = {time.id: {
            "nome": time.id,
            "jogos": 0,
            "vitorias": 0,
            "empates": 0,
            "derrotas": 0,
            "gols_marcados": 0,
            "gols_sofridos": 0,
            "saldo_gols": 0,
            "pontos": 0
        } for time in times}

        for jogo in jogos:
            if jogo.gols_casa is None or jogo.gols_visitante is None:
                continue

            time_casa = tabela[jogo.time_casa_id]
            time_fora = tabela[jogo.time_visitante_id]

            #jogos
            time_casa["jogos"] += 1
            time_fora["jogos"] += 1

            #gols
            time_casa["gols_marcados"] += jogo.gols_casa
            time_casa["gols_sofridos"] += jogo.gols_casa
            time_fora["gols_marcados"] += jogo.gols_visitante
            time_fora["gols_sofridos"] += jogo.gols_visitante

            #saldo
            time_casa["saldo_gols"] = time_casa["gols_marcados"] - time_fora["gols_sofridos"]
            time_fora["saldo_gols"] = time_fora["gols_marcados"] - time_casa["gols_sofridos"]

            #pontos
            if jogo.gols_casa > jogo.gols_visitante:
                time_casa["vitorias"] += 1
                time_casa["pontos"] += 3
                time_fora["derrotas"] += 1
            elif jogo.gols_casa < jogo.gols_visitante:
                time_fora["vitorias"] += 1
                time_fora["pontos"] += 3
                time_casa["derrotas"] += 1
            else:
                time_casa["empates"] += 1
                time_fora["empates"] += 1
                time_casa["pontos"] += 1
                time_fora["pontos"] += 1

        classificacao = sorted(tabela.values(), key=lambda x: (x["pontos"], x["saldo_gols"]), reverse=True)
        return classificacao


