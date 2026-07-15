from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """
    Contrato que toda subclasse deve respeitar:
    - pay(amount) recebe um valor numérico, sempre positivo.
    - Retorna um dicionário no formato:
          {"success": bool, "transaction_id": str}
    - Nunca lança exceção para um valor de amount válido (> 0).
    """

    @abstractmethod
    def pay(self, amount):
        pass

if __name__ == "__main__":
    # Demonstração: PaymentGateway é abstrata, não pode ser instanciada
    # diretamente. Capturamos o erro só pra mostrar a mensagem, em vez
    # de deixar o script crashar.
    try:
        gateway = PaymentGateway() # isso vai dar erro
    except TypeError as erro:
        print(f"Erro esperado: {erro}")
