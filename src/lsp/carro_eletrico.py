# =====================================
# 02 - Cumpre o contrato
# Classe derivada
# sobrescreve mas mantém a promessa
# ======================================

from carro import Carro

class CarroEletrico(Carro):
    def acelerar(self):
        self.velocidade += 10
        print("Acelerando em silêncio (motor elétrico)...")


carro_eletrico = CarroEletrico()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
print(carro_eletrico.velocidade)

# self.velocidade é um atributo
# le foi criado no __init__ da classe mãe (Carro),
# e como CarroEletrico não sobrescreve o __init__, 
# ele herda esse atributo normalmente (todo CarroEletrico nasce com velocidade = 0,
# sem a gente precisar reescrever nada disso).

# self.velocidade += 10
# Método scrito para manter a promessa / contrato

# Isso é justamente o motivo do CarroQuebrado ter quebrado: quando a gente sobrescreve um método,
# o Python não mistura automaticamente o comportamento antigo com o novo.
# Sobrescrever é "substituir o método inteiro", não "adicionar algo ao método antigo".
# Se você não escrever self.velocidade += 10 de novo, dentro do novo método, ela simplesmente não acontece.

#  super()
# Existe um jeito de reaproveitar o método da classe mãe em vez de reescrever ele do zero,
# chama super().