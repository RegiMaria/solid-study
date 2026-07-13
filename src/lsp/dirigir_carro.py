# =====================================
# 05 - O código cliente (versão reduzida)
# Confia no contrato: dirigir(carro) assume que a promessa é
# verdadeira (acelerar() sempre soma 10), sem checar qual
# subclasse recebeu.
#
# Aqui usamos só duas classes pra ver o "exame único" funcionando:
# - Carro:          define o contrato (promete)
# - CarroQuebrado:  quebra o contrato
#
# O importante: dirigir() é escrita UMA ÚNICA VEZ. Não muda nada
# dentro dela dependendo de qual carro chega -- é isso que simula
# a ideia de "código cliente que confia no contrato, sem saber
# qual subtipo específico está recebendo".
# ======================================

from carro import Carro
from carro_quebrado import CarroQuebrado
from carro_eletrico import CarroEletrico
from carro_eletrico_super import CarroEletricoSuper


def dirigir(carro):
    # __class__ é um atributo especial que todo objeto tem: aponta
    # pra classe que o criou. __name__ pega o nome dessa classe
    # como texto. Serve só pra identificar, no print, qual carro
    # está sendo testado em cada chamada.
    nome_da_classe = carro.__class__.__name__
    print(f"--- Dirigindo um {nome_da_classe} ---")

    carro.acelerar()
    carro.acelerar()
    carro.acelerar()

    print(f"Velocidade final: {carro.velocidade}")
    print("-" * 40)


# Bloco de teste protegido, pra não vazar print quando este arquivo
# for importado por outro (mesmo motivo do if __name__ == "__main__"
# que já usamos em carro.py).
if __name__ == "__main__":
    dirigir(Carro())               # cumpre o contrato -> velocidade final: 30
    dirigir(CarroQuebrado())       # quebra o contrato  -> velocidade final: 0
    dirigir(CarroEletrico())       # cumpre o contrato -> velocidade final: 30
    dirigir(CarroEletricoSuper())  # cumpre o contrato -> velocidade final: 30

# Todo carro sabe fazer acelerar(), e isso vai aumentar a velocidade.
# O dirigir.py faz isso: ele pega a mesma função, escrita uma única vez,
# e passa os quatro objetos diferentes pra ela, sem alterar nada dentro da função.
# É isso que prova (ou desmente) o LSP na prática porque simula exatamente a situação real:
# código genérico que recebe "um carro qualquer" sem saber de antemão qual subtipo é.
