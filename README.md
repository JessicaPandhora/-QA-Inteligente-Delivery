# QA Inteligente — Automação de Testes com IA

## Sobre o projeto

O QA Inteligente é um projeto prático de Quality Assurance (QA), desenvolvido para aplicar conhecimentos de testes funcionais, automação de testes, análise de requisitos e Inteligência Artificial como ferramenta de apoio ao processo de qualidade de software.

O projeto utiliza uma aplicação web simulada de delivery, desenvolvida em HTML e JavaScript, para validar funcionalidades de um carrinho de compras.

Além dos testes da aplicação, foram desenvolvidos módulos em Python para análise de requisitos, elaboração de prompts e geração estruturada de cenários de testes.

## Objetivos

- Desenvolver cenários de testes positivos, negativos e de limite.
- Aplicar testes automatizados com Python e Pytest.
- Automatizar interações com interfaces web utilizando Playwright.
- Validar comportamentos esperados de uma aplicação.
- Identificar ambiguidades e termos vagos em requisitos.
- Utilizar Inteligência Artificial como apoio à elaboração e revisão dos testes.
- Estruturar prompts para atividades de QA.
- Documentar evidências e resultados das execuções.

## Tecnologias utilizadas

- Python 3.14.2
- Pytest 9.2.0
- Playwright 1.65.0
- Chromium
- HTML5
- JavaScript
- GitHub Codespaces
- Git e GitHub
- ChatGPT como ferramenta de apoio com IA.

## Funcionalidades implementadas

### 1. Testes funcionais da aplicação

Arquivo: `tests/test_carrinho.py`

- Verificar se o carrinho inicia vazio.
- Validar a adição de produtos.
- Verificar o cálculo do total de dois produtos.
- Impedir a realização de pedidos com carrinho vazio.
- Validar a finalização de pedidos com produtos.

### 2. Testes de interface

Arquivo: `tests/test_interface_delivery.py`

- Verificar se a página Delivery abre corretamente.
- Validar se o carrinho inicia vazio na interface.
- Verificar se a adição de produtos atualiza quantidade e total.
- Validar a mensagem apresentada ao tentar finalizar um carrinho vazio.
- Verificar a finalização de pedidos com produtos.

Os testes de interface utilizam Playwright e o navegador Chromium para simular interações de usuários com a aplicação.

### 3. Módulo de criação de prompts

Arquivo: `ia/prompts.py`

Responsável por estruturar instruções para apoiar a elaboração de casos de teste, contemplando categorias e elementos necessários à documentação dos cenários.

### 4. Módulo de geração de cenários

Arquivo: `ia/gerador_cenarios.py`

Gera três categorias de cenários a partir de um requisito:

- Positivo.
- Negativo.
- Limite.

Os cenários são organizados com identificador, título, categoria, pré-condições, passos, resultado esperado e prioridade.

### 5. Módulo de análise de requisitos

Arquivo: `ia/analisador_requisitos.py`

Realiza uma análise inicial dos requisitos, identificando:

- Termos vagos ou subjetivos.
- Ausência de uma ação claramente definida.
- Requisitos com poucas informações.
- Recomendações para melhorar a clareza e a objetividade.

Nesta etapa, a análise utiliza regras implementadas em Python. A integração com IA generativa será uma evolução futura.

## Resultados dos testes

Última execução completa registrada em 10/11/2026:

- Total de testes executados: 27.
- Testes aprovados: 27.
- Testes reprovados: 0.
- Resultado: 27 passed.
- Tempo de execução: 7,34 segundos.

### Distribuição dos testes

| Módulo | Quantidade |
|---|---:|
| Testes do carrinho | 5 |
| Testes de interface | 5 |
| Testes de prompts | 5 |
| Testes do gerador de cenários | 6 |
| Testes do analisador de requisitos | 6 |
| **Total** | **27** |

**Status da última execução: todos os 27 testes aprovados.**

## Evidências

Os resultados das execuções são armazenados na pasta `evidencias/`.

Evidência principal:

`evidencias/execucao_completa_pytest.txt`

## Como executar o projeto

### 1. Instalar as dependências

```bash
pip install pytest playwright
```

### 2. Instalar o navegador Chromium

```bash
python -m playwright install chromium
```

### 3. Iniciar o servidor local da aplicação

```bash
python -m http.server 8000 --directory app
```

### 4. Executar todos os testes

Em outro terminal:

```bash
python -m pytest -v
```

### 5. Executar testes de um módulo específico

Exemplo:

```bash
python -m pytest -v tests/test_analisador_requisitos.py
```

O servidor local deve permanecer ativo durante a execução dos testes de interface.

## Estrutura do projeto

```text
QA-Inteligente-Delivery/
│
├── app/
│   └── index.html
│
├── ia/
│   ├── __init__.py
│   ├── prompts.py
│   ├── gerador_cenarios.py
│   └── analisador_requisitos.py
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
│   ├── test_interface_delivery.py
│   ├── test_prompts.py
│   ├── test_gerador_cenarios.py
│   └── test_analisador_requisitos.py
│
├── .gitignore
└── README.md
```

## Inteligência Artificial aplicada ao QA

O ChatGPT foi utilizado como ferramenta de apoio durante o desenvolvimento, contribuindo para a elaboração de cenários, estruturação de prompts, organização dos scripts, revisão das validações e documentação técnica.

Os módulos atuais de análise e geração utilizam lógica implementada em Python. A utilização de um modelo de IA generativa por integração externa está prevista para uma etapa futura.

A execução dos testes e a análise dos resultados são realizadas no ambiente de desenvolvimento, permitindo verificar os comportamentos implementados.

## Roadmap de evolução

### Nível 1 — Automação funcional

- Testes funcionais.
- Validação de regras de negócio.
- Automação de interface com Playwright.

### Nível 2 — Inteligência aplicada ao processo de QA

- Análise de requisitos.
- Identificação de ambiguidades.
- Estruturação de prompts.
- Geração de cenários positivos, negativos e de limite.
- Ampliação da cobertura de testes.

### Nível 3 — Integração com IA generativa

- Integração com um modelo de IA por API.
- Análise inteligente de requisitos.
- Geração de casos de teste com IA generativa.
- Revisão e melhoria dos cenários produzidos.
- Relatórios automatizados.
- Evolução da arquitetura e da documentação.

## Status do projeto

Em desenvolvimento.

Projeto desenvolvido para fins de estudo, prática profissional e construção de portfólio em Quality Assurance.
