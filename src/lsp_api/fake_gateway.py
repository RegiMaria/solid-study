# =====================================
# Implementação que VIOLA o contrato de PaymentGateway.
# Este é o "CarroQuebrado" da versão de pagamentos: sintaticamente
# respeita o contrato (herda de PaymentGateway, implementa pay()),
# mas quebra a promessa de duas formas diferentes.
#
# VIOLAÇÃO 1 - formato de retorno diferente do prometido:
#   O contrato promete {"success": bool, "transaction_id": str}.
#   Aqui devolvemos {"ok": bool} -- qualquer código cliente que
#   fizer resultado["success"] vai quebrar com KeyError.
#
# VIOLAÇÃO 2 - lança uma exceção que o contrato não previa:
#   O contrato diz "nunca lança exceção para amount > 0 válido".
#   Aqui, se o valor for maior que 1000, lançamos uma exceção --
#   algo que StripeGateway e PaypalGateway jamais fariam nessa
#   situação.
# ======================================

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
    
# Depois de escrever a classe faz o teste:
# python3 src/lsp_api/fake_gateway.py

# Bloco de teste
if __name__ == "__main__":
    gateway = FakeGateway()

    resultado = gateway.pay(150.0)
    print(resultado)  # {'ok': True} -- formato diferente do esperado

    try:
        gateway.pay(1500.0)
    except RuntimeError as erro:
        print(f"Erro inesperado: {erro}")