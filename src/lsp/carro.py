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
# meu_carro = Carro()
# print(meu_carro.velocidade)  # descomente pra ver que começa em 0

# Cada chamada de acelerar() soma 10 à velocidade DESTE carro (self = meu_carro)
# meu_carro.acelerar()  # velocidade: 0 -> 10
# meu_carro.acelerar()  # velocidade: 10 -> 20
# meu_carro.acelerar()  # velocidade: 20 -> 30

# print(meu_carro.velocidade)  # deve imprimir 30


# ---------------------------------------------------------------
# Todo arquivo que importava a classe Carro de carro.py, imprimia
# o resultado de carro.py.
# Por que este bloco está dentro de "if __name__ == '__main__':"
#
# Quando um arquivo Python é executado diretamente
# (ex: python carro.py), o Python cria uma variável especial
# chamada __name__ e dá pra ela o valor "__main__".
#
# Mas quando este arquivo é IMPORTADO por outro
# (ex: "from carro import Carro" dentro de carro_quebrado.py),
# o Python roda o arquivo inteiro pra registrar a classe Carro,
# porém __name__ passa a valer "carro" (o nome do módulo), não
# "__main__".
#
# Ou seja: esse "if" é um jeito de dizer:
#   "só rode este teste/demonstração se EU rodar este arquivo
#    diretamente. Se for só importado por outro arquivo,
#    NÃO rode -- só me dê a classe Carro."
#
# Sem esse "if", todo arquivo que importasse Carro ia
# acidentalmente executar essa demonstração também (foi
# exatamente o "30" que vazou lá no print do carro_quebrado.py).
# ---------------------------------------------------------------
if __name__ == "__main__":
    meu_carro = Carro()
    meu_carro.acelerar()
    meu_carro.acelerar()
    meu_carro.acelerar()
    print(meu_carro.velocidade)  # python3 carro.py deve imprimir 30 uma única vez.