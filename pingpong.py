'''
    Classe com os atributos e métodos do jogo Ping Pong.
'''
class PingPong():
    '''
        Recebe o placar atual no formato "aa:bb" e retorna uma string
        informando de quem é o saque atual.
    '''
    def saque(self, placar):
        pontos = placar.split(":")
        a = int(pontos[0])
        b = int(pontos[1])
        if a + b >= 40:
            if int(a + b) % 4 == 0 or int(a + b) % 4 == 1:
                jogador_a = True
            else:
                jogador_a = False
        else:
            if int((a + b) / 5) % 2 == 1:
                jogador_a = False
            else:
                jogador_a = True

        return "jogador a" if jogador_a else "jogador b"
