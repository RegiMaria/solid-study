# =====================================
# Segunda implementação concreta do contrato PaymentGateway.
# Simula o comportamento do PayPal: cumpre o mesmo contrato que
# StripeGateway, mas com uma lógica interna diferente -- é isso
# que o LSP permite: implementações diferentes por dentro, desde
# que o comportamento visível por fora respeite o contrato.
# ======================================
import uuid
from payment_gateway import PaymentGateway


class PaypalGateway(PaymentGateway):
    def pay(self, amount):
        print(f"[PayPal] Redirecionando pagamento de R$ {amount:.2f}...")
        transaction_id = f"pp_{uuid.uuid4().hex[:8]}"
        return {"success": True, "transaction_id": transaction_id}