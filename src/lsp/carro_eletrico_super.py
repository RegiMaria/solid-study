# =====================================
# 04 - Cumpre o contrato
# Como a função super() é uma ponte entre 
# a classe mãe e a filha:
#
# 1. super() → chama a função, que devolve o "objeto-ponte" 
# apontando pra Carro (a classe mãe de CarroEletrico)
#
# 2. .acelerar() → nesse objeto-ponte, você chama o método acelerar,
# que é o método original de Carro, não o sobrescrito
#
# super().acelerar()
# usando esse objeto pra chamar o método acelerar da classe mãe,
# não o sobrescrito
# ======================================

from carro import Carro

# SEM super() - reescreve tudo - descomente para testar
# class CarroEletrico(Carro):
#   def acelerar(self):
#       self.velocidade += 10
#       print("Acelerando em silêncio (motor elétrico)...")

# COM super() - reaproveita o comportamento da classe mãe
class CarroEletrico(Carro):
    def acelerar(self):
        super().acelerar()  # chama o acelerar() de Carro, que faz self.velocidade += 10
        print("Acelerando em silêncio (motor elétrico)...")

carro_eletrico = CarroEletrico()  
carro_eletrico.acelerar()
carro_eletrico.acelerar()
print(carro_eletrico.velocidade)