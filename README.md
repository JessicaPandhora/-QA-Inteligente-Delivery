
# QA Inteligente — Automação de Testes com IA

## Sobre o projeto

Este projeto tem como objetivo desenvolver conhecimentos práticos em Quality Assurance (QA), utilizando automação de testes com Python, Pytest e Playwright, além do apoio da Inteligência Artificial na elaboração e documentação dos cenários de teste.

O projeto simula operações de um aplicativo de delivery, com foco inicial na funcionalidade de carrinho de compras.

## Objetivos

- Desenvolver cenários de testes positivos e negativos.
- Automatizar testes utilizando Python e Pytest.
- Explorar ferramentas de automação de testes.
- Utilizar Inteligência Artificial como apoio ao processo de QA.
- Documentar resultados e identificar possíveis falhas.

## Tecnologias utilizadas

- Python 3.14.2
- Pytest 9.2.0
- Playwright 1.65.0
- GitHub Codespaces
- GitHub
- ChatGPT como ferramenta de apoio com IA.

## Testes implementados

Atualmente, o projeto possui cinco testes automatizados:

1. Verificação de carrinho inicialmente vazio.
2. Adição de produto ao carrinho.
3. Cálculo do total de dois produtos.
4. Impedimento de pedido com carrinho vazio.
5. Finalização de pedido com produto.

## Resultados

Primeira execução registrada:

- Total de testes: 5
- Aprovados: 5
- Reprovados: 0

Status: todos os testes passaram na execução realizada.

## Execução dos testes

Para executar os testes no ambiente Python:

```bash
python -m pytest -v
```

## Estrutura do projeto

```text
QA-Inteligente-Delivery/
├── documentacao/
├── evidencias/
├── relatorios/
├── tests/
│   └── test_carrinho.py
└── README.md
```

## Inteligência Artificial no QA

A Inteligência Artificial é utilizada como ferramenta de apoio na elaboração de cenários, revisão de scripts, interpretação de resultados e documentação técnica.

Os testes são executados e seus resultados são verificados para garantir que os comportamentos esperados estejam sendo atendidos.

## Status do projeto

Em desenvolvimento.

Novas funcionalidades, cenários de testes e melhorias serão incorporados gradualmente.

---

Projeto desenvolvido para fins de estudo e construção de portfólio profissional em Quality Assurance.

