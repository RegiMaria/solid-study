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