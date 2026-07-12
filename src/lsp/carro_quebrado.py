# =====================================
# 02 - Quebra o contrato 
# Classe derivada
# sobrescreve e trai a promessa
# ======================================

from carro import Carro

class CarroQuebrado(Carro): # herda de Carro
    def acelerar(self):
        print("Carro não liga, velocidade continua zero")

carro_quebrado = CarroQuebrado()
# print(carro_quebrado.velocidade)

carro_quebrado.acelerar()
carro_quebrado.acelerar()
carro_quebrado.acelerar()

print(carro_quebrado.velocidade)

#  Por que CarroQuebrado viola o LSP, mesmo o Python
# não acusando nenhum erro quando você roda o código?
#
# O método (da Classe Carro) promete um comportamento (contrato implícito):
# Toda vez que acelerar() é chamado, self.velocidade aumenta em 10.
# CarroQuebrado quebra esse contrato ao sobrescrever acelerar()
# sem manter a promessa original.
#
# CarroQuebrado.acelerar() quebra exatamente essa pós-condição: depois de chamado,
# velocidade continua igual. 
# O método existe, tem o mesmo nome, aceita os mesmos argumentos
# só não cumpre o que prometia(cada .acelerar() aumentar 10 e depois de chamado,
# velocidade aumenta em 10, essa é a pós-condição).
# Em resumo:
# Depois de chamar acelerar(), velocidade deve aumentar em 10.

# sobrescrever é permitido. Quebrar a promessa ao sobrescrever é que é o problema.

# Tipos de violação de LSP
# 1. Quebrar pós-condição (o que aconteceu aqui, o resultado prometido não se cumpre)
# 2. Fortalecer pré-condição (a subclasse passa a exigir mais do que a classe mãe exigia pra aceitar a chamada)
# 3. Quebrar invariante (uma regra que deveria valer sempre, tipo "velocidade nunca é negativa")