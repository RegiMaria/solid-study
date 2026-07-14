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

- [x] `carro.py` — classe base `Carro`, sem herança ainda. Fundamentos:
      classe, `__init__`, `self`, atributo, método, instanciação.
- [x] `carro.py` — corrigido vazamento de execução ao importar o módulo,
      usando `if __name__ == "__main__":`.
- [x] `carro_quebrado.py` — subclasse `CarroQuebrado(Carro)` que
      **viola** o contrato de `Carro` (sobrescreve `acelerar()` sem
      manter a promessa: velocidade nunca aumenta).
- [x] `carro_eletrico.py` — subclasse `CarroEletrico(Carro)` que
      sobrescreve `acelerar()` mas **cumpre** o contrato (reescreve
      `self.velocidade += 10` manualmente, só acrescenta um efeito
      colateral cosmético).
- [x] `carro_eletrico_super.py` — mesma ideia, mas reaproveitando o
      comportamento da classe mãe com `super().acelerar()` em vez de
      duplicar a lógica.
- [x] `dirigir_carro.py` — função cliente `dirigir(carro)`, escrita uma
      única vez, testada contra `Carro` e `CarroQuebrado` para provar
      o LSP na prática (mesma função, subtipos diferentes).
- [ ] Estender `dirigir_carro.py` para incluir `CarroEletrico` e
      `CarroEletricoSuper` na mesma bateria de testes.
- [ ] **Migrar o estudo para o exemplo mais realista em `lsp_api/`**
      (gateways de pagamento).

## Os scripts do exemplo Carro, em ordem

| Arquivo | Papel | Cumpre o contrato? |
|---|---|---|
| `carro.py` | Define o contrato (classe base) | — |
| `carro_quebrado.py` | Sobrescreve `acelerar()` e quebra a promessa | Não |
| `carro_eletrico.py` | Sobrescreve `acelerar()` reescrevendo a lógica original | Sim |
| `carro_eletrico_super.py` | Sobrescreve `acelerar()` reaproveitando com `super()` | Sim |
| `dirigir_carro.py` | Código cliente: confia no contrato, sem saber qual subtipo recebeu | — |

## Conceitos consolidados nesta etapa

- **Contrato implícito / pós-condição**: o que um método promete que
  será verdade depois de executado (`acelerar()` sempre soma 10 à
  velocidade).
- **Sobrescrever ≠ violar o LSP**: reescrever um método (`override`) é
  normal e permitido. O problema é reescrever de um jeito que quebra a
  promessa original da classe base.
- **Tipos de violação de LSP**:
  1. Quebra de pós-condição (o que aconteceu com `CarroQuebrado`)
  2. Fortalecimento de pré-condição (subclasse passa a exigir mais do
     que a classe mãe exigia)
  3. Quebra de invariante (uma regra que deveria valer sempre)
- **`if __name__ == "__main__":`**: evita que código de teste "solto"
  num módulo rode acidentalmente quando esse módulo é importado por
  outro arquivo.
- **`super()`**: função nativa do Python que devolve um objeto-ponte
  para a classe mãe, permitindo chamar o método original (não
  sobrescrito) de dentro da subclasse — evita duplicar lógica.
- **Papéis num cenário de LSP**:
  - quem **define** o contrato → a classe base (`Carro`)
  - quem **cumpre/quebra** o contrato → as subclasses
  - quem **confia** no contrato → o código cliente (`dirigir`)

## Próximo passo

Migrar o estudo para `lsp_api/`, um exemplo mais próximo do mundo real:
gateways de pagamento (`StripeGateway`, `PaypalGateway`) que respeitam
um contrato comum, e um `FakeGateway` que o viola — mostrando como o
mesmo problema do `CarroQuebrado` aparece em código profissional, com
consequências mais sérias (erro silencioso em processamento de
pagamento).