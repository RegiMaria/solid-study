# ===============================================
# Começamos com a classe Carro. Sem herança ainda.
#================================================

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

# Instanciando: cria um carro de verdade a partir da "receita" Carro.
# Nesse momento o Python roda o __init__ automaticamente,
# e meu_carro nasce com velocidade = 0.
meu_carro = Carro()
# print(meu_carro.velocidade)  # descomente pra ver que começa em 0

# Cada chamada de acelerar() soma 10 à velocidade DESTE carro (self = meu_carro)
meu_carro.acelerar()  # velocidade: 0 -> 10
meu_carro.acelerar()  # velocidade: 10 -> 20
meu_carro.acelerar()  # velocidade: 20 -> 30

print(meu_carro.velocidade)  # deve imprimir 30

