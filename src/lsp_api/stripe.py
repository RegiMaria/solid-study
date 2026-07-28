# =====================================
# Implementação concreta do contrato PaymentGateway.
# Simula o comportamento do Stripe: cumpre exatamente o que
# PaymentGateway promete, sem violar nada.
# ======================================
import uuid
from payment_gateway import PaymentGateway


class StripeGateway(PaymentGateway):
    def pay(self, amount):
        print(f"[Stripe] Cobrando R$ {amount:.2f} no cartão...")
        # uuid4() gera um identificador único aleatório.
        # .hex pega ele como texto, [:8] pega só os 8 primeiros
        # caracteres -- só pra deixar o id mais curto e legível.
        transaction_id = f"stripe_{uuid.uuid4().hex[:8]}"
        return {"success": True, "transaction_id": transaction_id}


if __name__ == "__main__":
    gateway = StripeGateway()
    resultado = gateway.pay(150.0)
    print(resultado)