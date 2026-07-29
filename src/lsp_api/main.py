# =====================================
# Código cliente: função escrita confiando SÓ no contrato de
# PaymentGateway, sem saber (nem se importar) qual implementação
# concreta vai receber. É exatamente isso que o LSP promete
# permitir -- e é exatamente isso que quebra quando o contrato
# é violado.
# ======================================

from payment_gateway import PaymentGateway
from stripe import StripeGateway
from paypal import PaypalGateway
from fake_gateway import FakeGateway


def processar_pagamento(gateway, amount):
    print(f"\n--- Processando pagamento de R$ {amount:.2f} com {gateway.__class__.__name__} ---")
    try:
        resultado = gateway.pay(amount)
        # Esta linha só existe porque confiamos 100% no contrato:
        # "todo gateway retorna um dict com chave 'success'"
        if resultado["success"]:
            print(f"Pagamento aprovado! ID: {resultado['transaction_id']}")
        else:
            print("Pagamento recusado.")
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")

# Bloco de testes

if __name__ == "__main__":
    # Gateways que RESPEITAM o contrato --> funcionam sem drama
    processar_pagamento(StripeGateway(), 150.0)
    processar_pagamento(PaypalGateway(), 300.0)

    # Gateway que VIOLA o contrato --> quebra o código cliente
    processar_pagamento(FakeGateway(), 150.0)   # KeyError escondido pelo try/except
    processar_pagamento(FakeGateway(), 1500.0)  # exceção que ninguém esperava

# processar_pagamento nunca mudou entre um teste e outro.
# é a mesma função, recebendo objetos diferentes.
# Isso é o LSP sendo demonstrado na prática, do início ao fim. :D