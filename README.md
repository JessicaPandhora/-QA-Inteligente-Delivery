
# QA Inteligente — Automação de Testes com IA

## Sobre o projeto

O QA Inteligente é um projeto de estudo e desenvolvimento de habilidades práticas em Quality Assurance (QA), com foco em testes funcionais, automação de testes e aplicação de Inteligência Artificial como ferramenta de apoio.

O projeto utiliza uma aplicação web simulada de delivery, desenvolvida em HTML e JavaScript, para validar funcionalidades de um carrinho de compras.

## Objetivos

- Desenvolver cenários de testes positivos e negativos.
- Aplicar testes automatizados com Python e Pytest.
- Automatizar interações com interfaces web utilizando Playwright.
- Validar comportamentos esperados de uma aplicação.
- Utilizar Inteligência Artificial como apoio à elaboração e revisão dos testes.
- Documentar evidências e resultados das execuções.

## Tecnologias utilizadas

- Python 3.14.2
- Pytest 9.2.0
- Playwright 1.65.0
- Chromium
- HTML5
- JavaScript
- GitHub Codespaces
- GitHub
- ChatGPT como ferramenta de apoio com IA.

## Testes implementados

Atualmente, o projeto possui dez testes automatizados, divididos em duas categorias.

### 1. Testes de lógica — Pytest

Arquivo: `tests/test_carrinho.py`

1. Verificar se o carrinho inicia vazio.
2. Validar a adição de produtos.
3. Verificar o cálculo do total de dois produtos.
4. Impedir a realização de pedidos com carrinho vazio.
5. Validar a finalização de pedidos com produtos.

### 2. Testes de interface — Playwright

Arquivo: `tests/test_interface_delivery.py`

1. Verificar se a página Delivery abre corretamente.
2. Validar se o carrinho inicia vazio na interface.
3. Verificar se a adição de produtos atualiza quantidade e total.
4. Validar a mensagem apresentada ao tentar finalizar um carrinho vazio.
5. Verificar a finalização de pedidos com produtos.

Os testes de interface utilizam o navegador Chromium para simular interações de usuários com a aplicação.

## Resultados dos testes

Última execução registrada:

- Total de testes executados: 10.
- Testes aprovados: 10.
- Testes reprovados: 0.
- Resultado: 10 passed.
- Tempo de execução: 8,02 segundos.

**Status: todos os dez testes passaram na execução registrada.**

## Evidências

Os resultados das execuções estão armazenados na pasta `evidencias/`.

Arquivo principal:

`evidencias/execucao_completa_pytest.txt`

## Como executar o projeto

1. Inicie o servidor local da aplicação:

```bash
python -m http.server 8000 --directory app
```

2. Em outro terminal, execute os testes:

```bash
python -m pytest -v
```

Para executar somente os testes de interface:

```bash
python -m pytest -v tests/test_interface_delivery.py
```

O servidor local deve permanecer ativo durante a execução dos testes de interface.

## Estrutura do projeto

```text
QA-Inteligente-Delivery/
│
├── app/
│   └── index.html
│
├── documentacao/
│   └── uso_ia_qualidade_testes.md
│
├── evidencias/
│   ├── execucao_pytest.txt
│   └── execucao_completa_pytest.txt
│
├── tests/
│   ├── test_carrinho.py
│   └── test_interface_delivery.py
│
├── .gitignore
└── README.md
```

## Inteligência Artificial aplicada ao QA

O ChatGPT foi utilizado como ferramenta de apoio durante o desenvolvimento, contribuindo para a elaboração dos cenários, organização dos scripts, revisão das validações e documentação técnica.

A execução dos testes e a análise dos resultados foram realizadas no ambiente de desenvolvimento, permitindo verificar os comportamentos implementados.

## Status do projeto

Em desenvolvimento.

Novos cenários, funcionalidades, melhorias e atividades de automação serão incorporados gradualmente.

---

Projeto desenvolvido para fins de estudo, prática profissional e construção de portfólio em Quality Assurance.

