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