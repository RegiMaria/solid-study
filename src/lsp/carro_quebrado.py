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