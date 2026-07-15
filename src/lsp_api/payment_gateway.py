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
