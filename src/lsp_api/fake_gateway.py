from payment_gateway import PaymentGateway


class FakeGateway(PaymentGateway):
    def pay(self, amount):
        if amount > 1000:
            # Nenhuma outra implementação faz isso -- surpresa
            # desagradável para quem confia no contrato.
            raise RuntimeError("FakeGateway não processa valores acima de 1000")

        print(f"[FakeGateway] fingindo processar R$ {amount:.2f}...")
        # Formato de retorno diferente do prometido pelo contrato
        return {"ok": True}

if __name__ == "__main__":
    gateway = FakeGateway()

    resultado = gateway.pay(150.0)
    print(resultado)  # {'ok': True} -- formato diferente do esperado

    try:
        gateway.pay(1500.0)
    except RuntimeError as erro:
        print(f"Erro inesperado: {erro}")