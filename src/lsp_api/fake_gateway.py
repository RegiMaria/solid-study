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