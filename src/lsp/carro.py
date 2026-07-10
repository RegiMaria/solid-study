# ===============================================
# Começamos com a classe Carro. Sem herança ainda.
#================================================

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

# Instanciando
meu_carro = Carro()
# print(meu_carro.velocidade)

meu_carro.acelerar()
meu_carro.acelerar()
meu_carro.acelerar()
print(meu_carro.velocidade)

