# Estudo do Princípio de Substituição de Liskov (LSP)

## Objetivo

Entender o LSP na prática, não só a definição de livro. A ideia é sair
sabendo:

- O que é o LSP.
- Que problema ele resolve (herança que "parece certa" mas quebra
  comportamento em produção).
- Como reconhecer uma violação de LSP em código real.
- Como corrigir uma violação (composição, contratos mais explícitos, etc).

## Estrutura planejada

```
src/
├── lsp/          -> exemplo didático simples (Carro)
└── lsp_api/      -> exemplo mais realista (gateways de pagamento:
                      Stripe, PayPal, e um gateway que viola o contrato)
```

A ideia de ter dois exemplos: primeiro fixar o conceito com algo simples
(Carro), depois ver como o mesmo problema aparece em código "de verdade"
(uma API de pagamentos, onde uma implementação que quebra o contrato
pode gerar bug sério e silencioso).

## Progresso até agora

- [x] Criada a classe base `Carro`, **sem herança ainda**. Só pra
      entender bem os fundamentos antes de introduzir o problema:
      classe, `__init__`, `self`, método, instanciação.
- [ ] Criar `CarroQuebrado(Carro)` — subclasse que viola o contrato
      de `Carro` (não altera a velocidade ao acelerar).
- [ ] Escrever `dirigir(carro)` — função "cliente" que confia no
      contrato de `Carro`, pra mostrar onde a violação quebra o código.
- [ ] Rodar os dois casos lado a lado e comparar o resultado.
- [ ] Repetir a ideia no exemplo mais avançado (`lsp_api/`), com
      gateways de pagamento.

## Estado atual do código (`carro.py`)

```python
# ===============================================
# Começamos com a classe Carro. Sem herança ainda.
# ===============================================

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

# Instanciando: cria um carro de verdade a partir da "receita" Carro.
# Nesse momento o Python roda o __init__ automaticamente,
# e meu_carro nasce com velocidade = 0.
meu_carro = Carro()
# print(meu_carro.velocidade)  # descomente pra ver que começa em 0

# Cada chamada de acelerar() soma 10 à velocidade DESTE carro (self = meu_carro)
meu_carro.acelerar()  # velocidade: 0 -> 10
meu_carro.acelerar()  # velocidade: 10 -> 20
meu_carro.acelerar()  # velocidade: 20 -> 30

print(meu_carro.velocidade)  # deve imprimir 30
```

## Próximo passo

Criar `carro_quebrado.py`, com uma classe `CarroQuebrado(Carro)` que
sobrescreve `acelerar()` de um jeito que quebra a promessa da classe
base e ver na prática por que isso é um problema de design, não só
um "bug".
